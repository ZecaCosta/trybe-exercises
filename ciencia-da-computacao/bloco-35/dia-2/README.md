# Herança, Composição e Interfaces

Vamos supor que precisamos criar um software que gera Relatórios de Vendas. Nosso programa tem que conter toda uma lógica para ler dados e criar o relatório e, ao final, gerar um arquivo imprimível com tais dados. Um JSON, por exemplo.

Considerando que estamos trabalhando com orientação a objetos, precisamos criar uma entidade para resolver este problema. Já que estamos fazendo um relatório, vamos começar fazendo dele a nossa entidade. Vamos, então, criar uma entidade SalesReport e tentar incumbir a ela a responsabilidade de gerar o nosso relatório.

```Python
import json


class SalesReport():
    def __init__(self, export_file):
        self.export_file = export_file + '.json'

    def build(self):
        """ Aqui colocamos a lógica para a entidade 'se criar',
        ou seja, criar um relatório imprimível. Por simplicidade,
        vamos omitir essa lógica nos exemplos! """
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    def serialize(self):
        # Vamos gerar, aqui, o nosso relatório em formato JSON
        with open(self.export_file, 'w') as file:
            json.dump(self.build(), file)

# Classe, crie (em outras palavras, instancie) uma nova entidade 'Relatório de vendas' para usarmos.

meu_relatorio_de_vendas = SalesReport('meu_relatorio')

# Entidade 'meu_relatorio_de_vendas', que acabou de ser criado, imprima-se.

meu_relatorio_de_vendas.serialize()
```
Algum tempo passou e surgiu a necessidade de além de gerar relatórios JSON, também gerar relatórios em CSV.

Será necessários estender o código. Algumas perguntas:

- Para adicionar a funcionalidade será necessaŕio mudar a assinatura (nome e parâmetros) de alguma função? Na hipótese da resposta ser sim, seria necessário mudar todos os códigos que usam essa função, e isso iria gerar muito retrabalho, conclusão, melhor não fazer a mudança assim.

- Os nomes das funções ainda estariam coerentes? Por exemplo, se uma for chamada de serialize_csv, a outra deveria se chamar serialize_json. Chamá-la só de serialize seria confuso, se temos mais de uma serialização, a serialize é qual delas?

- Seria necessário criar uma nova classe? Se sim, ela duplicaria alguma lógica? Se duplicar, por exemplo, a lógica de construção do relatório, na função build, não seria interessante.

- Seria necessário mudar o nome da classe? Se sim, voltaríamos ao problema de modificar código já existente, e isso não seria viável.

Resumindo se qualquer uma das coisas acima fossem feitas, a solução poderia trazer problemas. Alterar várias partes do código para adicionar uma funcionalidade, dá muito trabalho e aumenta a chance de se ter bugs.

Como sempre será necessario refatorar um código para introduzir uma nova funcionalidade. A missão, então, é outra: o código precisa ser escrito de uma forma que permita que extensões possam ser feitam sem modificar o código já existente. Assim, um trabalho de criação de nova funcionalidade que, no futuro, poderia durar várias horas, virará um trabalho de minutos.

Como fazer isso? Como escrever um código aberto para extensões, mas fechado para modificações?

A chave da questão é usar um dos grandes pilares da Programação Orientada a Objetos: `herança`

### Herança - Especialização de comportamentos
O que queremos tornar possível é estender nosso código sem modificar o que já existe. O código abaixo faz a mesma coisa que o código anterior, mas para resolver nosso problema foi refatorado para usar os conceitos de classes abstratas, métodos abstratos e o conceito de herança.

Para testar seu funcionamento, a classe foi instanciada e foi chamada sua função serialize.

Em Python, código abaixo pode ser testado no arquivo `sales_report_json.py`:

```Python
from abc import ABC, abstractmethod
import json


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)


# Para testar
meu_relatorio_de_vendas = SalesReportJSON('meu_relatorio')

meu_relatorio_de_vendas.serialize()
```
💡 Apesar de não ser usado neste exemplo, como boa prática, cada classe deve ser definida em seu próprio arquivo.

Herança nada mais é do que `especializar` o comportamento de uma classe. A classe herdeira é tudo que a classe ascendente é e um pouco mais.

Alguns exemplos:
- Se `FileCompressor` é a classe ascendente, `ZipFileCompressor` e `TarFileCompressor` são classes herdeiras. Ambas são um tipo específico de compressor de arquivos.

- Se `DatabaseConnector` é a classe ascendente, `MySQLConnector` e `MongoConnector` são as classes herdeiras. Ambas são um tipo específico de conector de banco de dados.

- Se `Model` é a classe ascendente, `UserModel` é a classe herdeira. É um tipo específico de model.

- Se `Service` é a classe ascendente, `AuthenticationService` é a classe herdeira. É um tipo específico de service.

💡 O Model Service Controller é uma arquitetura que usa como base a Programação Orientada a Objetos.

Programação Orientada a Objetos, portanto, nos dá o poder de criar classes herdeiras que especializam, mais e mais, o comportamento das classes ascendentes. Não há limite pra quantidade de classes herdeiras que uma classe pode ter, mas é crucial que tais classes sempre sejam uma especialização de comportamento 

No `Python`, definimos uma classe como herdeira da outra na linha que a define.
A lógica é: class ClasseHerdeira(ClasseAscendente).

No código do exemplo acima, a classe SalesReportJSON é herdeira da classe SalesReport, assim na sua linha de criação, isso é explicitado. Lembrando um bom e velho ditado da programação: "explícito é SEMPRE melhor do que implícito".

`class SalesReportJSON(SalesReport)`

### Classes Abstratas
No exemplo anterior vimos, além da herança, outras duas coisas meio confusas. Vimos que a classe ascendente principal parecia ser herdeira de outra, uma tal classe ABC. Além disso, a função serialize da classe ascendente está marcada como @abstractmethod e não tem código algum, ao contrário da classe herdeira.

O que seria isso?

Até agora, sempre tinhamos criado uma classe para que pudéssemos criar instancias dela para usarmos. Mas no exemplo acima, temos uma classe ascendente "geral", a SalesReport, e uma classe herdeira especifica, a SalesReportJSON. A partir do momento que temos comportamentos gerais e comportamentos especializados, ainda faz sentido usar a classe genérica?

Pensemos assim: o Relatório de Vendas precisa, obrigatoriamente, ter um formato. Temos uma classe geral SalesReport que define comportamentos dos relatórios de venda e suas classes herdeiras especializam-na para imprimirem o relatório em diferentes formatos. Nunca vamos ter um relatório geral, só um especializado.

Desta forma, não faz sentido instanciarmos um objeto da classe SalesReport e quando isso ocorre, dizemos que essa é uma classe abstrata. Ou seja, classe abstrata é a classe que não NUNCA poderá ser instanciada.

O que acontece se tentarmos instanciar uma classe abstrata?
Ocorrerá o seguinte erro:

> TypeError: Can't instantiate abstract class SalesReport with abstract methods serialize

E o método abstrato?
É a mesma coisa. É um método que nunca pode ser chamado diretamente. A classe SalesReport define o método serialize para deixar nítido que todo relatório de vendas deve ter uma forma de se serializar, mas ela mesma, por ser geral, não é serializável. Assim sendo, a classe SalesReport precisa definir a assinatura do método (nome e parâmetros), mas ele só será chamado sem erros se uma classe herdeira o implementar.

`Serializar`:
È o processo de mudar o formato dos seus dados para que possam ser armazenados ou enviados para serem, depois, convertidos de volta à sua forma original.
Fonte: Dicionário de Cambridge

No contexto de Programação Orientada a Objetos, devemos pensar que coisas abstratas são coisas criadas para serem especializadas por classes herdeiras.

Para exemplificar, podemos definir na classe SalesReport um segundo método abstrato chamado `get_length` para retornar quantos itens temos no relatório.

Tente chamar esse método a partir da classe herdeira SalesReportJSON, sem que esse método seja implementado. O seguinte erro ocorrerá:

> TypeError: Can't instantiate abstract class SalesReportJSON with abstract methods get_length

Depois que verificarmos o erro, podemos implementar uma lógica qualquer para esse método na classe herdeira SalesReportJSON e verificar que já é possível instanciá-la e até chamar o método.

# Interfaces
A Programação Orientada a Objetos dá muitos nomes para as coisas, e agora vamos aprender mais um. No exemplo acima nós definimos uma classe abstrata com um método abstrato. Vemos que a classe a ser especializada, a SalesReport, definiu a assinatura de uma função, mas não a sua lógica. Ou seja, todas as classes herdeiras podem colocar ali a lógica que quisessem, contanto que utilizassem a mesma assinatura de função.

Um objeto deve ser capaz de receber mensagens. As funções que chamadas  são as mensagens enviadas a ele. Quando damos a um objeto uma função, definimos uma mensagem que ele será capaz de receber e interpretar. Ao conjunto de mensagens que um objeto pode interpretar é dado o nome de `Interface`.

Podemos pensar na seguinte analogia: quando duas pessoas de países diferentes conversam, muitas vezes não é possível conversarem em seus idiomas nativos. Pode ser que um japonês e um brasileiro, por exemplo, só consigam se comunicar em inglês. Apenas somos capazes de nos comunicar com a outra pessoa se dissermos algo que ela seja capaz de entender. Com objetos, é a mesma coisa: a interface de um objeto representa o conjunto de mensagens que ele é capaz de entender. Para a classe SalesReport, sua interface é composta pelas funções build e serialize.

Um das vantagens da Programação Orientada a Objetos é que só precisamos saber como instanciar um objeto e quais funções ele tem. Falando a mesma coisa de maneira mais técnica, podemos dizer que a Programação Orientada a Objetos garante interfaces bem definidas para as várias partes do nosso programa se comunicarem sem que se precise saber como, internamente, cada parte funciona. Se as interfaces tem nomes bons e lógicas bem definidas, fica fácil reusar o código escrito. Não é preciso entender como ele funciona, só como me comunico com ele.

# E quando nem todas as herdeiras vão ter o mesmo comportamento?
Nossos relatórios estão muito grandes, então precisamos compactar todos os relatórios para transitar pelos servidores da empresa. Isso é super importante para economizar rede e disco. Vamos, então, dar aos nossos relatórios a capacidade de se comprimirem em arquivos `.gz`.

Em Python, código abaixo pode ser testado no arquivo `compressed_reports1.py`:

```Python
from abc import ABC, abstractmethod
import gzip
import json


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    def compress(self):
        binary_content = json.dumps(self.build()).encode('utf-8')

        with gzip.open(self.export_file + '.gz', 'wb') as compressed_file:
            compressed_file.write(binary_content)

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)


# Para testar
relatorio_de_compras = SalesReportJSON('meu_relatorio_1')

relatorio_de_compras.compress()
```
Adicionamos o comportamento à classe ascendente, pois todos os relatórios terão que ser comprimidos. Isso não é um comportamento especializado, é geral, então faz sentido torná-lo parte da interface da classe. O Python permite que classes abstratas tenham métodos concretos (ou seja, que métodos que façam coisas de verdade). As classes herdeiras não são obrigadas a re-implementar esses métodos, apenas os métodos abstratos.

Temos uma nova demanda. Precisaremos compactar os relatórios também em arquivos `.zip`. Assim, precisamos garantir que todos os relatórios sejam compactados em .zip e em .gz.

# Composição - Classes feitas de outras classes
Sabemos que não podemos criar, na classe mãe, uma função compress_zip para fazer o que precisamos. Se fizessemos isso precisaríamos mudar o nome da função compress para compress_gzip, e como consequência mudar todos os lugares onde essa função é chamada.

Poderíamos tentar especializar comportamentos. Pensar em fazer uma SalesReportJSONZip e uma SalesReportJSONGz. Mas e os outros formatos de relatório? Além disso, seria possível um nova demanda para compressão Winrar. Enfim, a herança não será suficiente pra resolvermos nosso problema.

Temos uma outra forma de compartilhar códigos na Programação Orientada a Objetos, a `Composição`.

Em Python, código abaixo pode ser testado no arquivo `compressed_reports2.py`:

```Python
from abc import ABC, abstractmethod
import gzip
import json
from zipfile import ZipFile


class ZipCompressor():
    ''' Nossos compressores terão fixado o local de salvamento
    do arquivo, então vamos defini-lo nos construtores'''
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor():
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)


class SalesReport(ABC):
    # Nossa classe agora espera *instâncias* de compressor como um parâmetro.
    # Temos um valor padrão para suportar o código que usava as SalesReport
    # sem parâmetros -- não precisa correr pra re-escrever nada ;)
    def __init__(self, export_file, compressor=GzCompressor()):
        self.export_file = export_file
        self.compressor = compressor

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    # Aqui temos um atributo de classe!
    FILE_EXTENSION = ''

    def get_export_file_name(self):
        # Aqui usamos o atributo de classe
        # Vai fazer mais sentido nas classes herdeiras!
        return self.export_file + self.FILE_EXTENSION

    def compress(self):
        self.serialize()
        self.compressor.compress(self.get_export_file_name())

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    # Nós não reimplementamos o get_export_file_name
    # mas como ele usa um atributo de classe pra pegar a extensão
    # só de redefinir o atributo já vamos conseguir mudar o resultado!
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.get_export_file_name(), 'w') as file:
            json.dump(self.build(), file)


# Para testar
relatorio_de_compras = SalesReportJSON('meu_relatorio_1')
relatorio_de_vendas = SalesReportJSON('meu_relatorio_2', ZipCompressor())

relatorio_de_compras.compress()
relatorio_de_vendas.compress()
```

Observe o que fizemos, nós criamos classes próprias para nossos compressores e passamos instâncias delas para nosso relatório. Isso, aliado ao nosso uso de parâmetros nomeados, nos permite, sem mudar código existente algum, dar a cada pessoa o poder de usar nossas classes e escolher se quer usar um compressor .gz , .zip, ou qualquer outro que vier no futuro.

A Herança serve para especializar comportamentos, onde toda classe herdeira deve fazer tudo que a classe ascendente faz. Quando precisamos reusar código, ou os comportamentos começam a aparecer em somente algumas das classes herdeiras, melhor usar Composição.

Neste caso, quem instancia a classe escolhe com qual dependência (no nosso caso, o compressor) quer usar. O nome disso é Inversão de Dependência. É uma inversão porque não é o autor da SalesReportJSON que define qual classe o método compress vai usar. Quem define é quem cria as instâncias da SalesReportJSON

# Composição e Interfaces
Nós falamos, qualquer outra classe de compressor que surgir funcionará com nosso código. Para isso acontecer, tal classe precisa, necessariamente, implementar a função `.compress()` com a mesma assinatura que nossas classes atuais.

O grande risco que temos ao fazer composição é a classe que passarmos para a outra não ter o mesmo formato que imaginamos, ou seja, se o novo compressor não tiver uma função chamada compress que receba o mesmo parâmetro que definimos, ao usá-la vai dar erro. Para garantirmos que isso nunca acontecerá precisamos definir uma `interface`.

Com uma classe abstrata, estabelecemos uma regra, todo compressor que for criado precisa ter uma função compress que receberá esse parâmetro específico para funcionar.

Assim usamos uma classe abstrata com um método abstrato para definir uma interface que, através de herança, definirá o comportamento de todos os compressores futuros, assegurando que sua composição sempre funcionará.

```Python
class Compressor(ABC):
    def __init__(self, filepath='./'):
        self.filepath = filepath

    @abstractmethod
    def compress(self, file_name):
        raise NotImplementedError


class ZipCompressor(Compressor):
    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor(Compressor):
    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)
```


# Métodos de Classe, Métodos Estáticos e Métodos de Instância

Mais um conceito útil. Como o local de criação do arquivo sempre será o mesmo, quer instanciemos um, dois, dez ZipCompressor, todas as instâncias serão absolutamente idênticas e farão a mesma coisa: terão o método compress com a assinatura que definimos. Sendo assim podemos invocar um método a partir de uma classe, e não de uma instância dela.

Para casos assim, podemos dizer que instanciar um objeto dessa classe é desnecessário. Tanto faz se invocamos a função com minha_instancia_de_zip_compressor.compress() ou ZipCompressor.compress().

Desta forma, podemos refatorar nosso código conforme a seguir. Esse código pode ser testado no arquivo `compressed_reports3.py`:

```Python

from abc import ABC, abstractmethod
import gzip
import json
from zipfile import ZipFile


class Serializer(ABC):
    @abstractmethod
    def serialize(cls, data):
        raise NotImplementedError


class ZipCompressor(Serializer):
    FILE_PATH = './'

    '''Um método de classe é chamado diretamente da classe,
    sem uma instância, e ACESSA algum atributo ou método da classe!'''
    @classmethod
    def compress(cls, file_name):
        '''Repare que, acima, o atributo cls é como o self: o
        cls é a própria classe, passada automaticamente para
        um método de classe, enquanto o self é a instância'''
        with ZipFile(cls.FILE_PATH + file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor(Serializer):
    '''Um método estático é chamado diretamente da classe,
    sem uma instância, e NÃO ACESSA nenhum atributo ou método da classe!'''
    @staticmethod
    def compress(file_name):
        '''Como métodos estáticos não acessam classe nem instância,
        o Python não dá a eles nenhum primeiro parâmetro'''
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)


class SalesReport(ABC):
    FILE_EXTENSION = ''

    def __init__(self, export_file, compressor=GzCompressor):
        self.export_file = export_file
        self.compressor = compressor

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    def get_export_file_name(self):
        return self.export_file + self.FILE_EXTENSION

    def compress(self):
        self.serialize()
        self.compressor.compress(self.get_export_file_name())


class SalesReportJSON(SalesReport):
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
    # implementação
    pass


# Para testar
relatorio_de_compras = SalesReportJSON('meu_relatorio_1')
relatorio_de_vendas = SalesReportJSON('meu_relatorio_2', ZipCompressor)

relatorio_de_compras.compress()
relatorio_de_vendas.compress()
```
Em resumo, métodos de classe são chamados diretamente da classe, sem instâncias, e utilizam algum atributo ou função auxiliar da classe para funcionar. Métodos estáticos são chamados diretamente da classe e não utilizam nada dela.

# Composição versus Herança
É muito comum, na Programação Orientada a Objeto, tentar usar herança para fazer o papel da composição, então devemos tomar cuidado. Utilizarmos herança para especialização e composição para compartilhamento de código.

Muitas vezes não é nítido qual é o caminho certo para a separação dos nossos objetos. Programar "no bom caminho" exige bastante prática e a aplicação de alguns princípios que ainda veremos nos próximos capítulos do conteúdo.

# Dicionário de conceitos
`Herança`
É uma forma de especializar o comportamento de uma classe (herdeira) com outra classe (ascendente).

Como o próprio nome já diz, é o princípio que define que uma classe deve ser capaz de herdar seus atributos e métodos de outra. E embora a classe base possa ter tanto métodos abstratos (que precisam ser implementados) quanto métodos concretos (que já estão implementados), a boa prática diz que a herança deve ser usada apenas para especialização. Se você quer apenas compartilhar código, use composição.

`Polimorfismo`
segundo o dicionário, a palavra "polimorfismo" significa "qualidade ou estado de ser capaz de assumir diferentes formas". Em POO, o polimorfismo é caracterizado quando duas ou mais classes contêm implementações diferentes para métodos com a mesma interface. Nos nossos exemplos pense, por exemplo, no método serialize, que é definido de forma abstrata na classe Serializer e assume diferentes formas nas classes JSONSerializer e CSVSerializer.

`Classe Abstrata`
Uma classe que não pode ser instanciada. Utilizada para definir as funções comuns (nem sempre abstratas) e suas assinaturas.


`Métodos Abstratos`
Um método, ou função, que precisa ser implemetado por uma classe herdeira para funcionar corretamente. Criado para definir uma Interface.

`Interface`
Conjunto de métodos que um determinado objeto "possui", ou, o conjunto de mensagens que um objeto é capaz de entender e responder.

`Composição`
Incorporar em um objeto outro objeto, para compartilhar código de maneira eficaz.

`Métodos de classe`
Métodos que podem ser chamados diretamente pela classe definida, e não por sua instância, para definirmos quando instânciar um objeto dessa classe for desnecessário. Uilizam, obrigatóriamente, atributos ou métodos internos da classe em seu funcionamento.

`Métodos estáticos`
Como os métodos de classe, mas não utilizam nada de sua classe em seu funcionamento.
