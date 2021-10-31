## Sumário de testes unitários usando Jest
Mais detalhes do Jest podem ser encontrados na [documentação oficial](https://jestjs.io/pt-BR) do Jest.

## Testes unitários: uma analogia ao relógio
Digamos que você, como pessoa desenvolvedora de software em um universo paralelo, seja uma pessoa relojoeira. A sua responsabilidade é confeccionar relógios de qualidade desde o zero, construindo desde as menores peças. Ao confeccionar as centenas de engrenagens, molas e parafusos que irão constituir seu relógio, você deve seguir especificações.
Cada unidade de engrenagens, molas e parafusos, ao serem confeccionadas, são testadas individualmente, medidas e verificadas, para garantir que irão funcionar conforme o esperado. Engrenagens devem suavemente girar, molas devem ter uma certa resistência, e parafusos devem ter diferentes espessuras e tamanhos, e por aí vai.
Como você poderia ter certeza de que cada pecinha do relógio está cumprindo sua devida função?
Com essa provocação, introduziremos você aos testes unitários, que tem a função de validar o comportamento do nosso código de forma sólida e precisa. Testes unitários são porções de código responsáveis por validar o comportamento de unidades funcionais de código.
Nesse contexto, entende-se como unidade funcional qualquer porção de código que, através de algum estímulo, seja capaz de gerar um comportamento esperado. Isso inclui funções, propriedades, construtores... tudo que, de alguma maneira, processe um comportamento de valor e que você deseja garantir que, apesar das alterações em nível de código, o comportamento siga sendo o mesmo.
Portanto, os testes unitários , assim como qualquer teste automatizado, permitem uma melhor manutenção do seu código. Eles não servem somente para verificar se uma função específica está funcionando, mas também para garantir que sua aplicação continue funcionando após alguma alteração. Sendo assim, é interessante pensar neles como um investimento de tempo para o futuro.

## Testando em pequenos passos
O TDD: Test Driven Development , em tradução livre, o desenvolvimento orientado a testes , é uma técnica de desenvolvimento que, em certos cenários, favorece a produtividade e a escrita de códigos confiáveis. Essa técnica é interessante porque ela ajuda a criar uma mente programadora orientada a testes , ainda que nem sempre escrever testes antes de escrever funcionalidades seja a prática mais adequada.
O TDD é muito importante como exercício e para determinados tipos de projetos, mas está longe de ser um consenso na comunidade programadora como prática fundamental para 100% dos casos. É importante que essa visão crítica fique bem clara.
Tendo isso em mente hoje você vai aprender e praticar o TDD, mas o conhecimento a ser absorvido é "como testar bem uma aplicação, de forma eficaz e produtiva" e "como ter um mindset orientado a testes", e não especificamente como a metodologia funciona.
Com muita prática e experiência, você irá desenvolver a intuição necessária para avaliar se o TDD é a melhor abordagem para testar a sua aplicação. Um exemplo interessante que o TDD pode ser bastante útil é no teste de funções puras.
O desenvolvimento orientado a testes é um processo cíclico que pode ser descrito em três etapas, como ilustrado abaixo. O princípio básico do TDD é fazer testes pequenos.

Destrinchando cada etapa, o TDD consiste em:
- Escrever um teste que cubra a função que você pretende implementar antes mesmo de executá-la. Este teste irá falhar - afinal, a sua função ainda não foi declarada. Você pode começar do teste mais elementar possível para esse cenário, como verificar se a função que você irá criar existe.
- Implementar apenas o necessário para que o teste passe. No caso do exemplo anterior, você só precisaria declarar a função para passar o teste.
- Refatorar o código para que ele esteja bem escrito e fácil de se entender. O pulo do gato nessa etapa é que você tem um teste já implementado que irá falhar caso você quebre algo ao refatorar o seu código.
- Repetir! Afinal de contas, o desenvolvimento orientado a testes é um ciclo. Volte a etapa 1 e repita esse processo até que todas as funcionalidades da sua função sejam implementadas.

Além de ser útil para testar funções puras, outro exemplo prático em que o desenvolvimento orientado a testes pode ser útil é consertar bugs. Os testes ajudam a quebrar problemas complexos em partes menores que podem ser analisadas mais facilmente. Assim, você poderá focar em uma regra de negócio específica sem medo de quebrar alguma outra funcionalidade.

## NodeJS Assert
Para começar, conheça um pouco sobre o NodeJS Assert.
O módulo Assert é uma ferramenta que testa expressões. Esse módulo já vem instalado com o NodeJS . Podemos entender o assert como sendo uma expressão booleana que será sempre true , a menos que haja uma falha.
Abaixo temos um exemplo de como podemos fazer um teste simples com assert:

```Javascript
const assert = require('assert'); // Sintaxe para incluir o módulo assert
'A escola que te
assert.strictEqual(50, 50); // Sem erros: 50 === 50
assert.strictEqual(50, 70); // AssertionError: 50 !== 70
```

Para o seu desenvolvimento durante o curso, será necessário o uso de ferramentas mais robustas, como o Jest , que você aprenderá na aula de hoje. Mas, caso tenha se interessado, você pode consultar mais sobre o NodeJS Assert aqui na [documentação](https://nodejs.org/api/assert.html).

## Introdução ao Jest
"Por que precisamos de um framework ? Não dá pra escrever todos os testes somente com asserts simples? "
Em teoria, sim. Mas à medida que suas aplicações se tornam maiores e mais complexas, esse processo torna-se inviável pelos motivos abaixo:

- Sua aplicação terá várias funções, provavelmente distribuídas por vários arquivos. Colocar todos os testes em um único arquivo torna-se impraticável rapidamente. Não é possível saber onde começam e onde terminam os testes de uma função. Mesmo em uma função mais complexa, você pode querer separar e agrupar testes relacionados;
- Node.js só executa um arquivo por vez, com o comando node <nome_do_arquivo> . Se há vários arquivos de teste, é preciso executar um por vez ou escrever um script shell para executar todos os arquivos;
- Você sempre precisa executar todos os testes de um arquivo. Não há como executar apenas um subgrupo dos testes presentes no arquivo;
- Sempre que um teste falha, a execução é interrompida imediatamente. Isso dificulta saber se os testes posteriores estão corretos, necessitando garantir que todos os testes anteriores estejam corretos;
- Vários testes podem requerer que os mesmos passos sejam executados antes ou após a execução, resultando em muita duplicação;
- Para pular ou desabilitar um teste falhando, é preciso removê-lo ou comentá-lo;
- Não há informações sobre a cobertura de testes. Ou seja, quais partes do código estão sendo estressadas pelos testes e quais não estão;

Para o mercado de trabalho, o assert é insuficiente. Normalmente os programas estão sempre evoluindo e ganhando novas features e, por conta disso, surgiu a necessidade de criar uma suíte de testes mais robusta, legível e de fácil manutenção.
Um framework de testes apresenta ferramentas para eliminar ou mitigar esses problemas. Existem várias ferramentas semelhantes, como Jest , Mocha e Jasmine . Entre eles, Jest se destaca por alguns motivos:

- É fácil de instalar e requer zero configuração, como você verá em breve;
- É rápido. O time de engenharia do Airbnb conseguiu diminuir o tempo de execução de sua suíte de testes de 12 para 4 minutos ao trocar Mocha por Jest ;
- Se integra muito bem com React . De fato, o Jest já vem instalado e configurado com o React. Não se preocupe se você não souber o que é o React, você aprenderá sobre ele em Front-end.

## Instalando o Jest
Para começar a instalar o Jest, você precisa ter o npm instalado e funcionando corretamente, abaixo temos um passo a passo, feito para Linux , sabendo disso, então vá ao seu terminal e digite o comando a seguir checar se o npm está instalado:

npm -v

Se ele te mostrar um número de versão (por exemplo, 6.14.15) está tudo certo. Caso ele retorne um erro dizendo que não encontrou o comando você deverá executar a instalação do npm

Primeiro vamos atualizar a nossa lista de repositórios:
sudo apt update

Agora com a lista de repositórios atualizada, vamos instalar o npm. Lembre-se que ao instalar com apt, você pode utilizar o comando de qualquer local, e em todas as próximas vezes você não deverá reinstalar, só execute esse passo caso não tenha o npm instalado ainda.
sudo apt install npm

Agora vamos simular a criação de um projeto que utilizará a biblioteca do Jest para os testes. Com o npm devidamente instalado e verificado, crie uma pasta e entre nesta nova pasta que você criou.

mkdir project-jest
cd project-jest

* Obs: É importante criar esta nova pasta para cada um dos seus projetos, pois além de ficar mais organizado, você vai evitar que as configurações de um projeto interfiram com outro, visto que o processo de instalação irá criar arquivos e pastas.

Após entrar na pasta, precisamos criar um novo package.json para o seu novo projeto.

O package.json é responsável por armazenar e descrever diversas informações de seu projeto, como a versão do node e do npm utilizadas, url do repositório, versão do projeto, dependências de produção e de desenvolvimento.
Para criar o package.json no seu projeto execute em seu terminal o comando abaixo:

npm init -y

Agora precisamos editar nosso package.json. Você deve ter observado que na chave "test" em "script" temos a seguinte informação: "test": "echo \"Error: no test specified\" && exit 1" . Isso significa que a nossa aplicação ainda não possui um script que defina como lidar com testes. Então vamos trocar essa informação por "test": "jest".

Por fim, vamos instalar o Jest , dentro da pasta que você criou no passo 3, executando o seguinte comando no terminal:

npm install --save-dev jest

Após rodar esse comando, vamos ver uma alteração importante que ocorreu no arquivo package.json . Para isso vamos abrir a pasta que você criou no seu VsCode com o comando abaixo:

code .

A sua pasta agora contém dois arquivos, o package.json e o package-lock.json e um novo diretório chamado node modules , estes últimos dois foram criados após você executar o comando npm install --save-dev jest.

Perceba que agora nosso arquivo package.json possui uma nova chave, "devDependencies" contendo o jest e a versão que está sendo utilizada neste projeto.

O "devDependencies" define os pacotes instalados no projeto como dependências de desenvolvimento. Ou seja, são pacotes que serão importantes apenas para o desenvolvimento do projeto. Existe também uma chave chamada "dependencies", que, diferente da primeira, lista os pacotes instalados como dependências de produção.

O node_modules é a pasta que guarda todos os arquivos baixados das dependências instaladas.

O package-lock.json é um arquivo que “trava” as versões das dependências. Quando outra pessoa executar npm install ou npm i para baixar as dependências, este arquivo garante que serão instaladas as mesmas versões para todo mundo.

Aqui vale ressaltar mais um ponto, o arquivo .gitignore que é utilizado para especificar arquivos ou diretórios que não queremos que sejam rastreados pelo git. É considerado uma boa prática no desenvolvimento, inserir a pasta node_modules em um arquivo .gitignore em todo projeto que você criar. Isso porque essa pasta contém centenas de arquivos e o processo de adicionar o seu projeto a um repositório remoto pode acarretar em mais tempo se você incluir essa pasta. Além disso, suponha que alguém vá realizar o clone do seu projeto, o processo também demoraria muito mais, visto que essa pasta contém muitos arquivos, mas pera aí, essa pasta não é importante porque guarda todos os arquivos das dependências instaladas? Sim, você tem razão, e é aí que os arquivos package.json e package-lock.json entram em cena. Ao clonar um projeto que contém dependências a serem instaladas, basta rodar dentro da pasta o comando npm install e todas as dependências e versões listadas nestes dois arquivos .json serão instaladas, criando a pasta node_modules.

## Escrevendo testes
Escrever testes em Jest é muito simples. Tudo que é necessário é utilizar a função test. A função it é um alias para test, ou seja, ambas se referem à mesma função e você pode usar qualquer uma delas. Essas funções, por serem globais, ficam automaticamente disponíveis nos seus arquivos uma vez que o Jest é instalado.

A função test espera três argumentos. O primeiro argumento é o nome do teste. Esse nome identifica o teste e é também o texto que aparecerá quando os testes forem executados. O segundo argumento é uma função contendo suas expectations. Em outras palavras, é dentro dessa função que você fará os testes propriamente ditos. O terceiro argumento (opcional) é um timeout , indicando quanto tempo o Jest deve esperar que o teste execute antes de abortá-lo.
Para entender melhor, vamos criar os arquivos sum.js e sum.test.js.

O Jest procura por arquivos com as extensões .js , .jsx , .ts e .tsx dentro de uma pasta com o nome __tests__ , ou arquivos com o sufixo .test ou .spec. É comum que o arquivo de teste tenha o mesmo nome e fique na mesma pasta do arquivo que está sendo testado, acrescido da sufixo .test.js.

Agora que você já viu um teste simples de jest em funcionamento, vamos praticar com mais um exemplo. O objetivo aqui é apenas mostrar o quanto trabalhar com a biblioteca Jest é mais simples.

Crie os arquivo com o nome 'loginValidation.js' e 'loginValidation.test.js'

Execute no seu terminal o comando npm test e veja o resultado. Ao rodar o teste você receberá a mensagem que todos os testes passaram. Apenas para verificar um caso de falha, altere no arquivo de teste a propriedade 'userName' do objeto 'user' para 'Bob", assim poderá ver que o teste vai falhar.

Outro ponto positivo da utilização do Jest para fazer nossos testes é que ele traz uma mensagem contendo um diff, ou seja, o que era esperado de ocorrer no teste e o que de fato aconteceu. Isso nos ajuda a entender mais rapidamente onde está o erro. Neste exemplo o teste esperava receber como valor um objeto contendo uma pessoa usuária com o nome "Joana", mas ao invés disso recebeu "Bob".

## Expect e matchers
Ao escrever testes, você precisa verificar que valores satisfazem a algumas condições. A função expect é utilizada para dar acesso a um conjunto de métodos chamados matchers. Esses métodos são estruturas de comparação utilizadas em diversas bibliotecas de testes, inclusive no Jest. Podemos pensar neles como uma ponte que dita qual é a relação entre o resultado que temos e o que queremos. O expect recebe o valor a ser testado e retorna um objeto representando uma expectation. Sobre esse objeto pode-se chamar os matchers fornecidos pelo Jest.

Vamos passar pelos matchers mais comuns. É interessante saber que existem muitos outros matchers que podem ser encontrados na [documentação oficial](https://jestjs.io/docs/expect) do Jest. No dia a dia, é normal quem desenvolve ler documentação, porque na maior parte das vezes esse é o local com mais informações atualizadas. Conforme as ferramentas que conhecemos passarem a ter mais opções de uso e funcionalidades, será normal recorrermos à documentação para aprendermos a utilizá-las melhor.

### Matcher toBe
Esse matcher, utilizado no exemplo anterior, é o matcher mais simples. Ele testa igualdade estrita entre o valor passado para expect e seu argumento. Isso significa, por exemplo, que um teste com o expectation abaixo falharia porque a string "5" não é igual ao número 5.

expect(5).toBe("5")

### Matcher toEqual
Para compreendermos a diferença entre toEqual e toBe, precisamos entender que no JavaScript existem duas formas de atribuir valores. A primeira é para a variável e a segunda é para propriedade do objeto, bem como ao passar argumentos para uma função. Essas formas de atribuição são conhecidas por valor e referência .
Para nos aprofundarmos nessas duas formas, é importante entender os tipos de dados, que separamos em tipos primitivos (Ex. number, string, boolean, etc) e objetos (Ex. Objetos, Funções, Arrays, etc).

Os tipos primitivos são imutáveis e sua atribuição ocorre por valor, ou seja, uma cópia do valor original. Portanto mesmo que o valor de uma primeira variável que tenha sido atribuido a uma segunda variável venha a ser alterado, o valor da segunda variável não mudará. Por exemplo:

``` JavaScript
let name = "Pedro";
let firstName = name;

name = "Carol";

console.log(name); // Carol
console.log(firstName); // Pedro
``` 

Por outro lado, os objetos tem atribuição por referência, ou seja, a cada vez que você cria um novo objeto, cria-se um novo espaço na memória para ele. Eles são mutáveis, por tanto podemos considerar que é uma forma de criar um apelido (alias) para o original, ou seja, você pode ser chamado pelo seu nome ou por seu apelido, mas você é uma pessoa única, não é possível criar um clone seu. Veja este exemplo:

``` JavaScript
let myName = { firstName: "Pedro" };
let identity = myName;

myName.firstName = "Carol";

console.log(myName.firstName); // Carol
console.log(identity.firstName); // Carol
```
Isso significa que objetos e arrays com conteúdo iguais são considerados diferentes no JavaScript. Para testar igualdade de objetos e arrays, é preciso usar o matcher toEqual, que acessa cada elemento do objeto ou array, fazendo um trabalho de comparação específico e que retorna uma resposta mais voltada para a necessidade dos testes:

``` JavaScript
test('array and object equality', () => {
  const arr = [1, 2 ,3];
  const obj = { a: 1, b: 2, c: 3};

  expect(arr).toBe([1, 2, 3]); // fails
  expect(obj).toBe({ a: 1, b: 2, c: 3}); // fails
  expect(arr).toEqual([1, 2, 3]); // OK
  expect(obj).toEqual({ a: 1, b: 2, c: 3}); // OK
});
```

### Valores booleanos
null, undefined e false são valores 'falsy'. Isso significa que são tratados como false sempre que se espera um valor booleano, como em condicionais. Às vezes, porém, é preciso distinguir entre eles. Jest fornece matchers específicos para cada um. Leia mais sobre eles na [documentação do Jest](https://jestjs.io/docs/using-matchers#truthiness).

### Números
Há matchers para as principais formas de comparar números. [Leia aqui](https://jestjs.io/pt-BR/docs/using-matchers#n%C3%BAmeros) sobre esses matchers.

### Strings
Para comparar string com expressões regulares, utilize o matcher toMatch, para mais detalhes consulte [aqui](https://jestjs.io/pt-BR/docs/expect#tomatchregexporstring).

### Arrays
Você pode verificar se um array contém um item em particular utilizando o matcher [toContain](https://jestjs.io/pt-BR/docs/expect#tocontainitem). Para verificar que um item possui uma estrutura mais complexa, utilize [toContainEqual](https://jestjs.io/pt-BR/docs/expect#tocontainequalitem). O matcher [toHaveLength](https://jestjs.io/pt-BR/docs/expect#tohavelengthnumber) permite facilmente verificar o tamanho de um array ou de uma string.

### Objetos
É bastante comum testar se um objeto possui uma propriedade específica. O matcher [toHaveProperty](https://jestjs.io/pt-BR/docs/expect#tohavepropertykeypath-value) é ideal para esses casos.

### Exceções
O matcher [toThrow](https://jestjs.io/pt-BR/docs/expect#tothrowerror) testa se uma função lança um erro quando é executada. Para testar se uma função está retornando um erro, é importante estar atento à sintaxe desse matcher:

``` JavaScript
const multiplyByTwo = (number) => {
  if (!number) {
    throw new Error('number é indefinido')
  }
  return number * 2;
};
multiplyByTwo(4);

test('testa se multiplyByTwo retorna o resultado da multiplicação', () => {
  expect(multiplyByTwo(4)).toBe(8);
});
test('testa se é lançado um erro quando number é indefinido', () => {
  expect(() => { multiplyByTwo() }).toThrow();
});
test('testa se a mensagem de erro é "number é indefinido"', () => {
  expect(() => { multiplyByTwo() }).toThrowError(new Error('number é indefinido'));
});
```
Note que para testar se um erro é lançado, passamos para o expect uma função. Chamamos multiplyByTwo dentro da arrow function. Devemos chamar a função diretamente dentro de expect, caso contrário, o erro não será detectado e a asserção falhará, porque o erro aconteceria antes mesmo de expect ser executado e ter a chance de capturar o erro. Para testar a mensagem de erro, como fizemos no terceiro teste do exemplo acima, usamos o matcher toThrowError e passamos dentro do parênteses a mensagem que será mostrada em caso de erro: new Error("number é indefinido").

* IMPORTANTE:  Para que os testes de deteção de erro funcionem corretamente, a função que queremos testar tem quer ser chamada indiretamente por uma arrow function, de dentro de expect.

### not
not permite testar o oposto de algo. Por exemplo, este código testa que domingo é um dia da semana, mas não um dia útil:

``` JavaScript
const workDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
const weekDays = ['Sunday', ...workDays, 'Saturday'];

test('Sunday is a week day', () => {
  expect(weekDays).toContain('Sunday');
});

test('Sunday is not a workday', () => {
  expect(workDays).not.toContain('Sunday');
});
```

## O bloco describe
A função describe cria um bloco para agrupar vários testes. Isso é útil para melhorar a organização dos seus testes. Você pode utilizar describe, por exemplo, para separar testes de funções diferentes em um mesmo arquivo, ou para agrupar testes relacionados dentro de uma função complexa que requer muitos testes. É possível aninhar blocos describe arbitrariamente. Dentro de cada bloco, qualquer declaração de variáveis ou funções é local a este bloco. Leia os exemplos na [documentação](https://jestjs.io/pt-BR/docs/api#describename-fn) do Jest para fixar.


