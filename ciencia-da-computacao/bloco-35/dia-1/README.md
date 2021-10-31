# Paradigmas de programação
Um paradigma é um estilo de programação, um modelo, uma metodologia, um conjunto de regras, uma forma de organizar. Não se trata de uma linguagem, mas sim a forma como solucionamos problemas usando uma determinada linguagem de programação.

Alguns dos paradigmas mais populares:
- Imperativo: um programa é uma sequência de comandos que alteram o estado atual do sistema até atingir um estado final.
- Estruturado: programas com uma estrutura de fluxo de controle e uso de procedimento e funções.
- Orientado objeto: organização através de objetos que contém dados, estados próprios e métodos que alteram ou recuperam os dados/estados. Os objetos comunicam entre si para compor a lógica do programa.
- Declarativo: especifica o que você quer, mas sem detalhar como fazer.
- Funcional: programas são avaliações de funções matemáticas sem alterar estados e com dados imutáveis.
- Lógico: especifica-se um conjunto de fatos e regras, o interpretador infere respostas para perguntas sobre o programa.

### Programação Orientada a Objetos (POO)
A Programação Orientada a Objetos é uma das formas mais populares do mundo de se programar, se não for a mais popular. Linguagens de programação como Java, Python, C++, Ruby e a clássica Smalltalk são fortemente voltadas para que se programe de forma orientada a objetos. Até mesmo linguagens como JavaScript, que não abraçam o paradigma completamente, são muito influenciadas por ele. As classes de JavaScript, para dar um exemplo, vem daí.

1. Reaproveitamento de códigos;
2. Criação de sistemas complexos;
3. Escalabilidade de sistemas;
4. Documentação;
5. Facilidade de mapear código através da abstração do mundo real.

`Abstração` é o ponto de partida para a criação de programas utilizando POO. Trata-se da capacidade de extrair dos personagens ou dos itens presentes no contexto, suas principais características, criando, dessa forma, objetos.

A programação orientada a objetos surgiu como uma alternativa as características da programação estruturada. O intuito da sua criação também foi o de aproximar o manuseio das estruturas de um programa ao manuseio das coisas do mundo real, daí o nome `OBJETO` como uma algo genérico, que pode representar qualquer coisa tangível.

Esse novo paradigma se baseia principalmente em dois conceitos chave: `classes e objetos`. Todos os outros conceitos, igualmente importantes, são construídos em cima desses dois.

### O que são classes e objetos?
Uma classe é uma descrição que abstrai um conjunto de objetos com características similares. Mais formalmente, é um conceito que encapsula abstrações de dados e procedimentos que descrevem o conteúdo e o comportamento de entidades do mundo real, representadas por objetos. De outra forma, uma classe pode ser definida como uma descrição das propriedades ou estados possíveis de um conjunto de objetos, bem como os comportamentos ou ações aplicáveis a estes mesmos objetos.

Imagine que você comprou um carro recentemente e decide modelar esse carro usando programação orientada a objetos. 

O seu carro tem as `características` que você estava procurando:
- um motor 2.0 híbrido
- azul escuro
- quatro portas
- câmbio automático

Ele também possui `comportamentos` que, provavelmente, foram o motivo de sua compra, como:
- acelerar
- desacelerar
- acender os faróis
- buzinar
- tocar música.

Podemos dizer que o carro novo é um objeto, onde suas características são seus `atributos` (dados atrelados ao objeto) e seus comportamentos são ações ou `métodos`.

Seu carro é um objeto que te pertence, mas na loja onde o comprou existiam vários outros, muito similares, com quatro rodas, volante, câmbio, retrovisores, faróis, dentre outras partes. Observe que, apesar do seu carro ser único (por exemplo, possui um registro único no Departamento de Trânsito), podem existir outros com exatamente os mesmos atributos, ou parecidos, ou mesmo totalmente diferentes, mas que ainda são considerados carros. Podemos dizer então que seu objeto pode ser classificado (isto é, seu objeto pertence à uma `classe`) como um carro, e que seu carro nada mais é que uma `instância` dessa classe chamada "carro".

Em Python
``` Python
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo;
        self.velocidade = 0

    def acelerar(self):
        # Codigo para acelerar o carro

    def frear(self):
        # Codigo para frear o carro

    def acenderFarol(self):
        # Codigo para acender o farol do carro
```
Astraindo um pouco a analogia, uma classe é um conjunto de características e comportamentos que definem o conjunto de objetos pertencentes à essa classe. Repare que a classe em si é um conceito abstrato, como um molde, que se torna concreto e palpável através da criação de um objeto. Chamamos essa criação de instanciação da classe, como se estivéssemos usando esse molde (classe) para criar um objeto.

No paradigma de orientação a objetos, tudo pode ser potencialmente representado como um objeto. Sob o ponto de vista da programação, um `objeto` não é muito diferente de uma `variável` no paradigma de programação convencional. 

Um programa orientado a objetos é composto por um conjunto de objetos que interagem através de "trocas de mensagens". Na prática, essa troca de mensagem traduz-se na invocação de métodos entre objetos.

### Mensagens e definição e importância

Uma mensagem é uma das responsabilidades de um objeto, possivelmente a mais importante, sendo utilizada para invocar um comportamento. Quando uma mensagem é enviada para um objeto, o mesmo pode ou não alterar seu estado.

É importante, pois orientação a objetos é sobre objetos e sua comunicação. E essa comunicação entre os objetos é feita através de mensagens.


Outro Exemplo: Objeto `PESSOA`
Informações, dados, características, propriedades, atributos ou estados que o objeto tem:
- nome
- idade
- data nascimento

Comportamentos, ações ou métodos aplicados ao objeto:
- atualizar nome
- remover foto
- adicionar documento

Qual é o ponto principal da POO?
É a troca de mensagens padronizadas entre OBJETOS.

Exemplo de comunicação entre dois OBJETOS:
Objeto PESSOA pede para o Objeto ENDEREÇO PESSOA alterar o número do CEP.

### Exemplo: recuperação de senha
Suponha que precisamos acrescentar a uma Aplicação Web uma funcionalidade de uma recuperação de senhas. Essa aplicação, no entanto, não está organizada com nitidez numa arquitetura como a MSC, então temos total liberdade para organizar nosso código. Mas não podemos perder de vista que a organização do código deve permitir fácil entendimento e uso dele.

Primeiramente, vamos definir em uma frase qual o problema que queremos resolver:

> Enquanto pessoa usuária, quero recuperar minha senha através de um email que receberei.

### Organizando a lógica em entidades
Não há forma certa ou errada de se organizar um código. Todas as suas formas tem seus benefícios e seus custos. Quer uma dica? Para pensar de forma Orientada a Objetos, para cada problema que se quer resolver, faça a seguinte pergunta:

`Quem quer fazer o que e com o que?`
No nosso caso, um User quer recuperar sua senha com seu email. Se partirmos daí, o que temos?
- Quem quer fazer? User
- O que que fazer? recuperar sua senha
- Com o que? seu email

### User, nossa primeira entidade
O que é a nossa entidade User? É alguém que quer recuperar uma senha por email. Esse alguém, portanto, tem um email e uma senha. Para identificarmos a pessoa, vamos dar um nome também. Esses são os atributos (informações a cerca da entidade). O Python nos dá ferramentas para criar entidades da forma como quisermos.

``` Python
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
```
No Python, a palavra reservada `class` é usada para definir `entidades`. Não uma entidade específica, uma pessoa específica, mas a entidade de uma forma um pouco mais abstrata, como vimos acima. "Uma entidade User contém um nome, um email e uma senha". A partir dessa definição, para criarmos uma entidade específica, precisamos `estanciar` (atribuir a uma variável) nossa classe, como no código abaixo:

``` Python
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

meu_user = User("Ari", "ari@dominio.com", "Senha")
print(meu_user)  # <__main__.User object at 0x7f477e6c2070>
print(meu_user.name)  # Ari
print(meu_user.email)  # ari@dominio.com
print(meu_user.password)  # Senha
print(type(meu_user)) ## <class '__main__.User'>
```

Criamos uma variável (meu_user) que contém a entidade. Temos nela os valores, os dados daquela entidade. Já vimos variáveis que são números, que são strings, que são muitas coisas, mas nossa variável é uma `entidade`. Nossa variável é um `Objeto`.

### Objetos no Python
O que fizemos no exemplo anterior foi definir uma entidade de forma geral e criar uma entidade específica para nossa variável. Usando a nomenclatura correta, dizemos que definimos uma `classe` ("entidade de forma geral") e criamos, a partir dela, um `objeto` ("uma entidade específica", criada a partir de uma definição geral de entidade, ou seja, de uma classe).

Toda classe capaz de criar objetos deve possuir um `método construtor`, que será chamado quando o objeto estiver sendo criado.

No caso de Python, o método construtor é, `SEMPRE`, definido com o nome __init__ no topo da classe que se está criando. Por trás dos panos, o Python utilizará a sua lógica para criar e retornar um objeto, ou seja:

```Python
class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python."""
        self.name = name
        self.email = email
        self.password = password

# Para invocar o método construtor, a sintaxe é NomeDaClasse(parametro 1, parametro 2, parâmetro n)
# Repare que o parâmetro self foi pulado, outro detalhe do Python.
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")

# Resumindo: A variável `meu_user` contém o objeto criado pelo construtor da classe User.
```
### Enviar emails - onde coloco essa lógica?
Se temos uma entidade User que quer enviar emails de recuperação de senha, partimos do princípio que essa entidade saiba enviar emails. Para uma entidade saber fazer algo, precisamos definir nela uma função que represente essa ação. Essa função é conhecida como método (coisas que a entidade faz). Algo assim:

``` Python
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email de reset de senha")


meu_user = User("Ari", "ari@dominio.com", "Senha")
meu_user.reset_password()
```
Se definimos uma função numa classe, podemos chamá-la a partir do objeto que criamos. Quando pedimos para um objeto fazer algo, dizemos que estamos `enviando uma mensagem` àquele objeto.

__Atenção para isso! Na essência, toda lógica da orientação a objetos parte do envio de mensagens entre objetos.__

No código acima, estamos pedindo para `meu_user` resetar sua senha. Não nos interessa como a ação será feita, só nos interessa que ela será feita. Podemos imaginar duas pessoas escrevendo esse código. A pessoa que cria o objeto e pede que ele resete sua senha não precisa saber como ele faz isso, pois temos uma classe bem nomeada, com uma função bem nomeada, e isso basta. Ao invés de gastar tempo precioso entendendo seu código, essa pessoa pode usá-lo sem esforço.

``` Python
class User:
    # Não preciso saber como a classe funciona.

    def reset_password(self):
    # A classe tem essa função? Ótimo, é o que basta.


# Já sei o suficiente pra agir.
meu_user = User("Ari", "ari@dominio.com", "Senha")
meu_user.reset_password()
```
Agora imagine uma aplicação com dez entidades, não seria viável sabermos como cada uma funciona para utilizá-las.Basta saber seus atributos e qual função usar e o resto acontece `automagicamente`.

Esse é o poder da Programação Orientada a Objetos. Quando chamamos uma função de um Service, numa aplicação MSC, e a usamos sem saber como ela estava feita, no fundo, o que fizemos foi usufruir do benefício da Programação Orientada a Objetos, que embasa o MSC.

Toda arquitetura que tenha como base a Programação Orientada a Objeto quer definamos entidades e as usemos sem entender como elas funcionam.

### Os quatro pilares da Programação Orientada a Objetos 

1. Abstração:
A abstração consiste em um dos pontos mais importantes dentro de qualquer linguagem Orientada a Objetos. Como estamos lidando com uma representação de um objeto real, temos que imaginar o que esse objeto irá realizar dentro de nosso sistema.

São três pontos que devem ser levados em consideração nessa abstração:

- O primeiro ponto é darmos uma identidade ao objeto que iremos criar. Essa identidade deve ser única dentro do sistema para que não haja conflito.

- A segunda parte diz respeito a características do objeto. Como sabemos, no mundo real qualquer objeto possui elementos que o definem. Dentro da programação orientada a objetos, essas características são nomeadas propriedades. Por exemplo, as propriedades de um objeto “Cachorro” poderiam ser “Tamanho”, “Raça” e “Idade”.

- Por fim, a terceira parte é definirmos as ações que o objeto irá executar. Essas ações, ou eventos, são chamados métodos. Esses métodos podem ser extremamente variáveis, desde “Acender()” em um objeto lâmpada até “Latir()” em um objeto cachorro.

2. Encapsulamento:
O encapsulamento é uma das principais técnicas que define a programação orientada a objetos. Se trata de um dos elementos que adicionam segurança à aplicação em uma programação orientada a objetos pelo fato de esconder as propriedades, criando uma espécie de caixa preta.

A maior parte das linguagens orientadas a objetos implementam o encapsulamento baseado em propriedades privadas, ligadas a métodos especiais chamados `getters e setters`, que irão retornar e setar o valor da propriedade, respectivamente. Essa atitude evita o acesso direto a propriedade do objeto, adicionando uma outra camada de segurança à aplicação.

3. Herança:
O reuso de código é uma das grandes vantagens da programação orientada a objetos. Muito disso se dá por uma questão que é conhecida como herança. Essa característica otimiza a produção da aplicação em tempo e linhas de código.

Para entendermos essa característica, vamos imaginar uma família: a criança, por exemplo, está herdando características de seus pais. Os pais, por sua vez, herdam algo dos avós, o que faz com que a criança também o faça, e assim sucessivamente. 

4. Polimorfismo
Outro ponto essencial na programação orientada a objetos é o chamado polimorfismo. Na natureza, vemos animais que são capazes de alterar sua forma conforme a necessidade, e é dessa ideia que vem o polimorfismo na orientação a objetos. Como sabemos, os objetos filhos herdam as características e ações de seus “ancestrais”. Entretanto, em alguns casos, é necessário que as ações para um mesmo método seja diferente. Em outras palavras, o polimorfismo consiste na alteração do funcionamento interno de um método herdado de um objeto pai.

### Mailer - Criando mais entidades
Ainda precisamos criar a lógica de envio de email.
Para codarmos um envio de email vamos usar dois módulos, o `ssl` e o `smtplib`. Ambos nos permitirão logar num servidor de emails e, de lá, fazer um envio de forma segura através da rede. Para conseguirmos fazer isso, precisaremos ter em mãos algumas informações: o email enviador, a senha do email enviador, o email que receberá a mensagem, o assunto e o corpo do email.

Precisamos dessas informações à disposição, então vamos colocar elas no nosso construtor para, então, criar a lógica da nossa ação.

Veja o arquivo `mailer1.py` para detalhes.

Feitas as devidas configurações no servidor do email essa lógica funciona, mas temos um problema, estamos criando uma entidade User. Para criá-la, estamos passando seu nome, email, senha, email de envio de reset de senha e a senha desse email. Se tivermos mil users teremos sempre o mesmo email de reset e a mesma senha. Ou seja, o construtor de User está lotado de atribuições. E cada instância que criarmos vai ter uma cópia das informações do enviador de emails

Para organizar nosso código, sempre devemos lembrar do primeiro pilar de POO, a Abstração. Se uma lógica parece não pertencer a uma entidade, extraia-a para uma outra entidade, ou para uma entidade nova.

No nosso caso, seria interessante criar um enviador de emails. O nome mais literal possível que podemos dar para uma entidade que envia emails é Enviador de Emails, Mailer em inglês.

Sobre as Mensagens, qual seria mais simples? "User, resete sua senha!" ou "Enviador de emails, resete a senha deste User!". Ambas são corretas, mas a primeira, do ponto de vita do encapsulamento é melhor. A pessoa que vai usar nosso código não precisa saber que, por trás dos panos, há uma entidade Mailer trabalhando. Na segunda implementação seria necessário que ela soubesse disso. A primeira alternativa exige que a pessoa saiba menos da nossa lógica e, portanto, a encapsula melhor.

Sendo assim, nosso exemplo ficaria como apresentado no arquivo `mailer2.py`.

### Mensagens e Métodos
Cada objeto pode receber mensagens.
O `meu_user.reset_password()`, por exemplo, pode ser lido como "Meu user, resete a sua senha!". Dentro da classe User, definimos a função reset_password que irá conter a lógica de resetar senha. Quando mandamos uma instância de User resetar a senha, essa função sabe o que deve ser feito.

Funções que "respondem mensagens" se chamam `Métodos`. Usualmente ela será nomeada com um verbo ('Reset your password!' vira reset_password, por exemplo).

No contexto de POO, todas as interações são feitas por troca de mensagens. Isso significa que enviamos uma mensagem para um objeto ou não fazemos nada com ele. O bom Encapsulamento faz com que nós só precisemos saber do nome de uma classe e seus métodos para interagir com ela. 

No Python, mesmo quando alteramos um atributo diretamente, por trás dos panos o que ele faz é enviar uma mensagem de atualização para a classe.


### Dicionário de conceitos
Na Programação Orientada a Objeto muitas coisas tem nome, e é importante sabermos quais são, são jargões importantes para uma boa comunicação.

`Classe`
É uma entidade "geral" que definimos com base no problema que queremos resolver. Consiste numa espécie de molde para criação de novos objetos, definindo seus atributos e métodos comuns que serão utilizados por ele.

`Objeto/Instância`
É uma entidade "específica", criada a partir das regras definidas pela classe (entidade "geral"). De forma análoga, podemos pensar que a classe é o molde e o objeto a escultura que o molde faz.

Uma vez criada uma classe criada, podemos instanciar um objeto. Instanciar é o ato de criar um novo objeto/instância a partir de uma classe definida.Quando criamos um objeto a partir de uma classe, podemos dizer que esse objeto é uma instância dessa classe. Ou, também podemos dizer que a classe instanciou um objeto.

`Atributo`
Atributos são onde as informações de uma instância criada são armazenadas, representam o estado do objeto.
No exemplo de recuperação de senha, as classes armazenam as seguintes informações:
- User: Uma instância de User armazena informações de nome, email e senha de cada pessoa usuária da nossa aplicação;
- Mailer: Uma instância de Mailer armazena as informações de quem envia e quem recebe o email, seu assunto e seu conteúdo.

`Método`
Métodos são funções que possuem acesso aos dados armazenados em atributos, podendo implementar comportamentos e alterar seus estados.

Como um método realiza uma ação, a utilização de verbos é uma boa prática para nomeá-los. Nomes como redefinir_senha ou reset_password poderiam ser utilizados para um método que implementa o comportamento de redefinição de senha.

`Construtor`
É um método especial utilizado para inicializar instâncias de uma classe e que pode receber parâmetros usados para definir as informações armazenadas em seus atributos.

`Abstração`
Pilar da Programação Orientada a Objetos. Se refere a sempre criar entidades que farão as ações que resolverão seu problema.

Este conceito está ligado à definição de características de uma classe de forma abstrata, que significa definir uma classe focando nas mensagens que ela responde e nos atributos de que precisa.

`Encapsulamento`
Pilar da Programação Orientada a Objetos. Se refere a poder instanciar uma entidade e enviar mensagens a ela sem saber como ela funciona por dentro.

Trata-se de esconder parte da implementação de uma classe, exibindo de forma pública somente aquilo que é necessário para que o cliente consuma sua classe e deixando detalhes da implementação protegidos ou privados.

`Mensagem`
Forma com que objetos interagem, chamando funções uns dos outros. Um chamado como esse é um envio de mensagem a outro objeto. "User, resete sua senha!"