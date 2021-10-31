### Verbos HTTP:
	app.verbo(rota, callback);
	callback tem parâmetros obrigatórios (req, res);

### ROTAS:

Rota padrão ou raiz ou home
	"/", normalmente rota GET
	normalmente no arquivo index.js
	
### Pasta routes:
	usada para separar a rotas em arquivos individuais;
	as rotas devem ser exportadas: module.exports = app;
	as rotas devem importadas no index.js: const simpsons = require('./routes/simpsons');
	para chamar as rodas usa-se: app.use('/simpsons', simpsons);
	sendo que '/simpsons' é a raiz da rota e simpons se referencia oa arquivo;
	caso seja necessário receber json, pode habiltar diretamente no index:
		app.use(express.json());

### CRUD verbos HTTP
	post:	 create
	get:	 read
	put:	 update
	delete:  delete

#### POST:
	app.post('/', rescue(async (req, res) => {
	    const size = data.length;
	    data[size] = {
		id: `${size + 1}`,
		name: req.body.name
	    }

	    try {
		await fs.promises.writeFile(`${__dirname}/../data/simpsons.json`, 
		JSON.stringify(data));
		res.status(201).send({
		    message: 'Salvo com sucesso!'
		})
	    } catch (error) {
		throw new Error(error);
	    }
	}));

	transformar uma função assíncrona em sincrona (esperar resultado), usando async-await
	como pode ser necessário tratar erro já se usa try-catch
	como é necessário salvar (writeFile) no arquivo será necessário importar file system:
	o writeFile não parte da pasta local e sim da raiz do projeto, faz-se necessário usar dirname;
	__dirname: traz o caminho completo do diretório desde a raíz do projeto


#### GET:
	app.get('/', (req, res) => {
	    res.status(200).send(data);
	});

#### PUT:
	app.put('/:id', async (req, res) => {
	    const { id } = req.params;
	    const { name } = req.body;
	    data[id - 1].name = name;

	    try {
		await fs.promises.writeFile(`${__dirname}/../data/simpsons.json`,
		JSON.stringify(data));
		res.status(200).send({
		    message: 'Salvo com sucesso!'
		})
	    } catch (error) {
		throw new Error(error);
	    }
	});
	
	como o id é passado pela url é recuperado pelo params;
	retorna código 200 OK

#### DELETE: 
	app.delete('/:id', async (req, res) => {
	    const { id } = req.params;
	    const index = id - 1;
	    data.splice(index, 1);

	    try {
		await fs.promises.writeFile(`${__dirname}/../data/simpsons.json`,
		JSON.stringify(data));
		res.status(204).send()
	    } catch (error) {
		throw new Error(error);
	    }
	});
	
	data.splice(index, 1): exclui um elemento a partir de index;
	retorna código 204 No Content

### MIDDLEWARE:

Pasta middleware:
	para segregar os middlewares (error, log, auth, etc), apenas por questão de organização;
	é obrigatório a exportação da constante usado para criar o middleware;
	quando tiver mais de um middleware é boa prática criar um arquivo index.js;
	esse arquivo é um agregador de middleware's que facilitará a importação;

No arquivo index.js da raíz do projeto:
	além de importar os middleware's, será necessário habilitar pra uso;
		app.use(middlewares.logMiddleware);
		app.use('/simpsons', simpsons);
	a habilitação dos middlewares deve ser antes das rotas que o utilizarão;
	a exceção é o middleware de erro que deve ser habilitado depois das rotas antes do listen;
		app.use(middlewares.errorMiddleware);
		app.listen(port, () => {
		    console.log(`App rodando na porta ${port}`);
		});
	usar função rescue pra captar erro. Pacote express-rescue deve ser instalado/importado;

	
	

	
