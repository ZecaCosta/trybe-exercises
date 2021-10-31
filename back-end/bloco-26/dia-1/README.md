### JavaScript:
- Linguagem criada originalmente para o Front-End;
- Roda direto no navegador.

### Node.js:
- Ambiente de execução criado em 2009 para interpretar JavaScript;
- O uso do JavaScript no servidor (Back-End) intensificou a partir de 2011;
- Node.js utiliza o mesmo motor do Chrome, V8.

### NPM
Node Package Manager

- criar pasta para um novo projeto Node.js e rodar comando:
	npm init -y 
  cria o arquivo package.json

- instalar pacotes necessários no projeto:
	npm i readline-sync
	cria a pasta node_modules
	cria o arquivo package-lock.json
  a pasta node_modules não vai subir(upload) para o GitHub

- criar arquivo principal na raiz do projeto:
	index.js

- dentro do arquivo index.js importar os pacotes necessários:
	const readline = require('readline-sync');

### REVISÃO JAVASCRIPT

concatenação de string e variáveis
	console.log('Coeficientes: A:' + a + ' B:' + b + ' C:' + c);
	console.log(`Coeficientes: A: ${a} B:${b}, C:${c}`);
	console.log('Coeficientes: A:%s B:%s C:%s',a,b,c);
	console.log(`\nCoeficientes: A: ${a}, B: ${b}, C: ${c}\n`
\n para pular linha
	    console.log(`Resultado: \n\tx1 = ${resultado.x1}, \n\tx2 = ${resultado.x2}`);
\t para tab

interromper IF sem a necessidade de usar ELSE
	return;
	
retornar duas variáveis:
	return [x1, x2]; ou return {x1, x2};