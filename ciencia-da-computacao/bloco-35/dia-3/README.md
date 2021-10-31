#### Liskov Substitution Principle
É o L dos princípios S.O.L.I.D. 

Suponha que o seu time de desenvolvimento está trabalhando em um software que controla os acessos à API do seu serviço. Você está responsável por manter um código cujo dever é gerar uma token de acesso, que o front utilizará para validar todas as requisições que receber de clientes.
Sua empresa cobra clientes por número de requisições, então você precisará registrar em um banco a quantidade de vezes que uma determinada token foi utilizada para acessar o serviço. Porem, o seu time considerou os seguintes fatos:

- infra-estrutura utiliza um servidor SQL, cuja inserção tende a ser mais lenta.

- É normal que clientes acessem o serviço milhares de vezes em um intervalo de 30 minutos, e depois fiquem vários dias sem utilizar.

Diante desses fatos, decidiu-se guardar as contagens de requisições em um banco de dados cache, que fica armazenado por inteiro na memória RAM de uma máquina. Por estar nessa memória, ele é super rápido, mas não pode ser muito grande. Assim o valor é armazenado no banco em cache e, após o valor ficar uma hora inteira sem ser atualizado, ele é enviado para o banco SQL.

A seguinte classe é usada para acessar o banco de dados SQL:

```Python
import pysql  # Encare essa lib como fictícia!

class SqlConnector:
    # ...

    def __init__(self, address, port):
        print(f'criada uma conexão em {address}:{port}')
        self.db = pysql.connect(address, port)

    def get_count(token):
        query = f'SELECT count FROM access WHERE token={token};--'

    def count_request(token):
        query = f'UPDATE access SET count = count+=1 WHERE token={token};--'
        self.db.execute(query)
```
Nosso dever é implementar o acesso ao Redis, nosso banco de dados cache , e oferecer uma interface amigável e fácil de utilizar. 

`Redis` é um banco de dados em memória, que utiliza uma estrutura chave-valor.

Assim, criamos a seguinte classe, implementando a lógica de cache:

```Python
import pyredis  # Encare essa lib como fictícia também!

class RedisConnector:
    def __init__(self, address, port):
        print(f'criada uma conexão em {address}:{port}')
        self.db = pyredis.connect(address, port)

    def get_count(token):
        result = self.search(token)
        amount = result.get("access_count", None)
        return amount

    def update_count(token):
        amount = self.get_count()
        if amount is None:
            self.db.insert({token:1})
        else:
            self.db.insert({token: amount+1})
```

Feedback recebido:
Vamos ter que refatorar muita coisa! Usamos o conector SQL em muitos lugares, e será necessário usar o conector Redis em todos eles. Se o nome das funções mudarem, teremos que refatorar o código inteiro. Se pudéssemos chamar os dois conectores da mesma forma, nos mesmos lugares? Isso facilitaria demais.

Com este feedback, refatoramos as classes conectoras. Vamos criar uma classe Connector, que abstrai os métodos que devemos utilizar numa interface, e os dois conectores serão herdeiros desta classe. Veja:

```Python
from abs import ABS, abstractmethod

class Connector(ABS):
    @abstractmethod
    def get_count(token):
        pass

    @abstractmethod
    def count_request():
        pass

class RedisConnector(Connector):
    def __init__(self, address, port):
        # A lógica da conexão ao banco Redis

    def get_count(token):
        # A lógica de acesso ao banco Redis

    def count_request(token):
        # A lógica de acesso ao banco Redis

class SqlConnector(Connector):
    def __init__(self, address, port):
        # A lógica da conexão ao banco SQL

    def get_count(token):
        # A lógica de acesso ao banco SQL

    def count_request(token):
        # A lógica de acesso ao banco SQL
```
Agora, uma classe que precisar acessar o banco pode receber como Connector tanto uma classe quanto a outra! Veja um exemplo de uso:

```Python
import analyzer

# o parâmetro database é um connector
def analyze_data(token, database, data):
    try:
        report = analyzer.complete_report(data)
        database.count_request(token)  # Cliente receberá cobrança
        return report

    # Se a database não tiver o método count_request, vai lançar o erro
    # AttributeError -- e a gente deixa o programa travar se isso acontecer.
    except analyzer.InvalidDataException:
        # A gente lida apenas com InvalidDataException, que é um erro
        # esperado quando o relatório não estiver pronto.
        return  # Cliente não receberá cobrança, pois não geramos o relatório
```
Note como, dentro deste código, não conseguimos distinguir qual conector estamos usando. Tudo o que nos interessa aqui é que ela tem um método count_request() que recebe a token de acesso. Assim, se estivermos trabalhando nesta parte da aplicação, podemos ter certeza de a inserção em banco foi feita, sem nos preocuparmos com a lógica de cache que está acontecendo por trás.

Acabamos de utilizar o L da arquitetura SOLID.

Princípio de substituição de Liskov: objetos em um programa devem ser substituíveis por instâncias de suas classes herdeiras sem que isso quebre nada. O que quer dizer, para que esta substituição seja possível, os subtipos devem seguir a interface de um tipo base. Ou seja, classes herdeiras devem sempre respeitar a interface de suas classes ascendentes! Elas podem especializar comportamentos, mas nunca removê-los.

### Interface Segregation Principle

Problema:
o banco de dados SQL está recebendo acessos demais, causando sobrecarga e crashes.

Solução:
Uma réplica do banco de dados. Como a maioria dos acessos é de de leitura, então com esta réplica read-only, poderemos dividir os acessos entre cada um dos dois, evitando a sobrecarga. Aí quando for um acesso de escrita, podemos contar com o replicador pra manter os dois bancos iguais.

Pra atender essa demanda, os trechos do sistema que só precisam ler dados utilizam conectores que só conseguem ler, evitando confusões. 

Só que nós temos uma interface de conector que implementa operações de leitura e escrita. E agora precisamos de uma interface somente com leitura, sem escrita! Como conseguimos fazer isso?

Primeiro, devemos considerar a abstração em que trabalhamos ao atender as demandas anteriores. Devemos manter uma boa abstração, para que o nosso codigo continue simples e fácil de manter. Então, nosso objetivo principal é assegurar duas coisas:

- As classes ReadOnlyConnectors devem implementar apenas o método get_count.

- Já as classes que forem FullConnectors devem implementar, pelo menos, get_count e count_request.

Classes Abstratas e Herança são formas que temos de garantir que as classes herdeiras precisam ter certos comportamentos. Vamos tentar abstrair estes comportamentos.

```Python
''' ABC é uma Abstract Base Class. Herdar desta classe indica que estamos fazendo
uma classe abstrata, que neste caso também é uma Interface, pois não contem
implementações, apenas definições de métodos.

Estes metodos DEVEM ser implementados pelas classes herdeiras, por isso
utilizamos o decorator `@abstractmethod`: se estes metodos não forem sobrescritas por
uma implementação da classe herdeira, o Python nos avisará que estamos cometendo um erro.'''

from abc import ABC, abstractmethod

class ReadOnlyConnector(ABC):
    @abstractmethod
    def get_count(self, token):
        pass

# Como FullConnector deve também ser capaz de ler,
# ela é uma classe abstrata que herda de outra classe abstrata!
class FullConnector(ReadOnlyConnector):
    @abstractmethod
    def count_request(self, token):
        pass

## Uma classe abstrata exige a implementação de todos os seus métodos.
## Uma implementação incompleta não poderá ser instanciada!
## class SQLConnector(FullConnector):
##     def count_request(self, token):
##         ...
##
## TypeError: não pode instanciar porque não implementa o método get_count
## sql = SQLConnector()
```
Esta divisão de tarefas onde cada interface tem a responsabilidade de representar uma única característica é chamada de Princípio De Segregação de Interfaces, ou em inglês, Interface Segregation Principle. Justamente o I dos princípios S.O.L.I.D.

Interfaces, como toda abstração, são "contratos" feitos em código para que possamos nos organizar melhor. As interfaces garantem que tudo estará organizado, e respeitando estes contratos. Não faça interfaces grandes, faça interfaces pequenas com responsabilidades únicas

### Review:

A seguir os 5 princípios S.O.L.I.D., para relembrar e reflitir como todos eles se complementam para nos ajudar a escrever um código que precisará de menos refatorações conforme o sistema cresce e muda ao longo do tempo.

- S: Single Responsability Principle - Princípio da Responsabilidade Única;

- O: Open/Closed - Aberto para extensão, fechado para modificação;

- L: Liskov's Substitution Principle - Principio da Substituição de Liskov;

I - Interface Segregation Principle - Principio da Segregação de Interfaces;

D - Dependency Inversion - Inversão de Dependências (ou: use composições).

### O que são Padrões de Projeto
Padrão de Projeto é uma solução geral para um problema que ocorre com frequência dentro de um determinado contexto no projeto de software. Desde a década de 70, cientistas da computação perceberam que, ainda que em contextos diferentes, algumas soluções de problemas se repetiam em vários softwares. Visando facilitar a reutilização do desenho da solução e a comunicação, assim como melhorar a documentação e compreensão de um sistema, essa comunidade de cientistas começou a catalogar estes padrões.

Para deixar tudo mais tangível, responda à seguinte pergunta: "Quantas aplicações no mundo precisam iterar sobre uma lista de elementos?"

Certamente milhares, senão milhões, correto? Eventualmente se propôs uma forma padronizada de implementar a solução para este problema, e tal proposta foi adotada, e este é o padrão de projeto conhecido como `iterator`.

Ao receber uma lista de entidades, uma classe que implementa o padrão de projeto iterator deve ter uma interface específica: por exemplo, uma função next que retorna o próximo elemento da dita lista.

Não interessa se a sua lista é em formato de array, de árvore, se é uma lista de inteiros, objetos ou o que for. Ao garantir que sua classe possui um iterador, você garante que ela tem uma função next que vai acessar o próximo elemento da sua lista. A forma de fazer isso é você quem define. Ao seguir o padrão de projeto, você organiza o seu código - e o seu raciocínio - de uma forma pensada, estudada e comprovadamente eficaz.

O exemplo do iterator é um exemplo mais básico do que padrões de projeto são, mas ilustra bem o seu propósito:

Organizar seu código e raciocínio de formas eficazes, comprovadamente boas e (praticamente) universalmente aceitas. Ao se deparar com um determinado problema que se encaixa na definição de um padrão de projeto, busque o padrão de projeto para saber uma forma boa de resolver esse problema.

Um padrão é definido e documentado com um nome, o problema que busca resolver, uma solução dada por ele e as consequências sobre esta escolha. São documentados em formas de explicações e diagramas abstratos, possibilitando assim a utilização em diferentes contextos.

Quando falamos de Padrões de projeto, é impossível deixar de falar sobre o livro da 'gangue dos quatro'. Hoje em dia, porém, muitos outros padrões estão documentados em diversas outras literaturas. É importante conhecer diferentes padrões e onde se aplicam, mas não fique preso a eles. Outros padrões podem emergir dos seus códigos e nem sempre estarão documentados.

### iterator
Pessoas que trabalham na parte de cobrança de clientes, nos trouxe uma demanda nova, dizendo:

"Costumavamos fazer os relatórios de cobrança a clientes de forma manual, mas isso se tornou impossível com o crescimento de clientes que aconteceu 3 meses atrás. Estamos com um atraso de 3 meses de relatório! Agora nossa empresa comprou uma ferramenta automática de relatórios, mas o meu computador não conseguiu carregar 3 meses de tabela para fazer o relatório! Só tenho 2 GB de memória."

Depois de debater soluções com o time, entendemos que o problema é o tamanho do que está sendo carregado no servidor em que o Beto trabalha. Não podemos carregar os 300 GB de dados do banco, então decidimos que vamos precisar separar o resultado da consulta em partes pequenas, pegando uma de cada vez, para alimentar a aplicação de relatórios que roda no PC com 2 GB.

```Python
class DatabaseIterable:
    def __init__(self, sql_connector, query_template):
        self.db = sql_connector
        self.query_template = query_template

    def get_page(self, page):
        return self.db.get(query=self.query_template, page=page)

    def __iter__(self):
        """Aqui iniciamos a iteração, retornando um objeto DatabaseIterator
        como Iterador."""

        return DatabaseIterator(self.db)


class DatabaseIterator:
    def __init__(self, sql_connector):
        """No construtor da classe iteradora definimos o valor inicial do
        contador current_page, e também o(s) atributo(s) que será(ão)
        responsável(is) por armazenar/acessar a coleção de dados pela qual
        queremos iterar."""

        self.db = sql_connector
        self.current_page = 0

    def __next__(self):
        """Este método busca no banco de dados a página que queremos e
        incrementa o contador current_page, para retornarmos a próxima página
        na próxima vez que o método for chamado."""

        data = self.iterable.get_page(page=self.current_page)

        """É uma boa prática a utilização da exceção StopIteration() para
        indicar que não foi possível avançar na iteração. Ou seja: tentamos
        acessar uma current_page que não existe."""

        if not data:
            raise StopIteration()

        self.current_page += 1
        return data
```
Esse negócio de acessar partes pequenas de um conteúdo maior, uma de cada vez, acho que já vimos isso em algum lugar, não?

Veja abaixo e teste com o arquivo `iterator.py`

```Python
minhas_linguagens = ["javascript", "python", "C", "Go"]
for linguagem in minhas_linguagens:
    print("Eu sei programar em: ", linguagem)

lista_de_compras = open("compras.txt", "r")
for item in lista_de_compras:
    print("Eu devo comprar: ", item)
```

