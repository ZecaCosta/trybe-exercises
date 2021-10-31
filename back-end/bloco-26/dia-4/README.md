### Express:
	framework oficial do Node.js criado em 2010;
	apesar de oficial não faz parte do padrão Node.js;
	assim precisamos instalar: npm install express;
	depois instalado para iniciar o express em uma aplicação, serão necessários 3 passos:
		- importar pra dentro do aplicação:
			const express = require('express');
		- atribuir o express a uma constante, por conveção, chamamos esta constante de app:
			const app = express();
	para completar a estrutura mínima, será necessário levantar o servidor:
			app.listen(3000, () => {
    			console.log('App rodando na porta 3000')
			});
	obs.: ver arquivo starter.js

### Postman:
	como os navegadores puros só funcionam com verbo http GET;
	usa-se o postman para testar apis com todos verbos http.

### Endpoint:
	no contexto da programação back-end é chamado de rota;
	a seguir exemplo de uma rota raíz ou home usando o verbo get pra enviar resposta ao front-end
		app.get('/', (_req, res) => {
  		  res.send("Hello World!");
		});
	o verbo sempre terá uma rota e um callback;
	os parâmetros mínimos do callback são req (entrada) e res (saída) (nesta ordem);
	esses nomes req e res são por convenção, poderiam ser qualquer um;
	quando um parâmetro não é usado, pode-se inibir com underline;
	o status padrão é 200 OK, mas poderia enviar o status: res.status(200).send("Hello World!");
	obs.: ver arquivo get-basic.js;
	
### Atualização do arquivo:
	quando o arquivo é carregado apenas com o node (node arq.js) será necessário reiniciar o 		servidor, derrubando e carregando novamente;
	para auxiliar o servidor existe uma biblioteca (pacote) externa chamada nodemon (hot reload);
	como é auxiliar, devemos instalar o pacote: npm install nodemon -D;
	obs.: o -D é para que esse pacote fique apenas em nível de desenvolvimento (devDependencies); 		ou seja, este pacote não estará disponível quando o servidor for colocado em produção;
	para carregar o arquivo: nodemon arq.js

### Middleware:
	middleware é uma função compartilhada entre várias rotas pra evitar repetição de código;
	para criar atribuimos a uma constante, abaixo exemplo de middleware de autenticação:
		const authMiddleware = (req, res, next) => {
    		  console.log('Entrei no middleware!');
    		  next();
		};
	será necessário ativar o middleware para uso, normalmente antes das rotas:
		app.use(authMiddleware);
	obs.: notar que o middleware tem um parâmetro a mais, o next (uso obrigatório na função)
	
### Router:
	permite segregar um middleware para determinada(s) rota(s);
	é padrão do node.js, portanto não é necessário instalar;
	basta importar para uma constante: const router = express.Router();
	especificar um middleware router.use(authMiddleware);
	especificar uma rota específica
		router.get('/dash', (_req, res) => {
  		  res.send("admin dashboard!");
		});
	
	habiltar router para uso: app.use('/admin', router);
	obs.: quando for acionar no postman. a rota deve ser /admin/dash

### Middleware de erro:
		const errorMiddleware = (err, req, res, next) => {
    		  console.log('Entrei no middleware de erro!');
    		  next();
		};

	obs.: notar que o middleware de erro tem um quarto parâmetro, err
	será necessário ativar o middleware de erro para uso, mas obrigatoriamente no final das rotas:
		app.use(authMiddleware);

### Rescue:
	pacote externo que permite tornar uma rota assíncrona, usando os async;
	o rescue é uma função, portanto será necessário colocar a callback dentro;
	como é externo é necessário instalar npm install express-rescue;
		app.get('/error', rescue(async (req, res) => {
    		  throw new Error('Errrrrrrrrrou!');
		}));
	é necessário importar para uma constante: const rescue = require('express-rescue');
	
### BodyParse:
	ficou deprecated a partir da versão 4 do express;
	o express tem um middleware nativo para acessar o body de uma requisição front-end;
	obrigatoriamente o verbo http tem que ser POST:
		app.post('/node', (req, res) => {
    		  console.log(req.body);
    		  res.send(req.body);
		});
	e será necessário habilitar o middleware para uso: app.use(express.json());
	obs.: .post('/node' e .get('/node' são rotas diferentes;
	logicamente que front-end precisa definir o json do body;

### Processo básico de configuração
npm init -y | para iniciar um novo projeto node.js

npm install express | para instalar framework express

npm install nodemon -D | para instalar a dependência nodemon. A flag -D indica que é uma dependência de desenvolvimento

node index.js | para rodar o projeto

npm start | quando "start": "node index.js" está no scripts do package.json

npm run dev | quando a dependência nodemon está instalada e "dev": "nodemon index.js" está no scripts do package.json

npx nodemon index.js | roda sem necessidade de instalar o nodemon

Npm is a tool that use to install packages.
Npx is a tool that use to execute packages.
Packages used by npm are installed globally you have to care about pollution for the long term.
Packages used by npx are not installed globally so you have to carefree for the pollution for the long term

Como parar o processo node rodando na porta 3000 ou qualquer outra porta?

1-) primeiro encontrar process ID (PID), pelo comando: lsof -i tcp:3000
resposta: 

COMMAND PID  USER         FD   TYPE DEVICE SIZE/OFF NODE NAME
node    7420 josecarlos   19u  IPv6 135788 0t0      TCP *:3000 (LISTEN)

2-) depois "matar" o processo com o comando: kill -9 PID, no caso kill -9 7420


