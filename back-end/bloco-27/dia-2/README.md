### INSTALAÇÃO BÁSICA: banco de dados MONGODB

npm init -y && npm install express && npm install nodemon -D && npm install mongodb

"dev": "nodemon index.js", | no arquivo package.json no objeto Scripts

criar arquivo index.js na raíz do projeto

### ESTRUTURA BÁSICA: criar estrutura básica dentro do index.js

importar as rotas:
const routes = require('./routes'); | ao importar desta forma, virá todo o objeto exportado no arquivo index.js da pasta routes.

habilitar as rotas pra uso:
app.use(routes.songRoutes); | como foi importado todo o objeto é necessário definir qual rota está sendo habilitada, no caso a songRoutes.

### CRIAR ESTRUTURA DE PASTAS: arquitetura de camadas (MSC)

Pasta config:
pra criar o arquivo de configuração para conexão com o banco de dados;
nome padrão do arquivo: conn.js;
definição do nome do banco de dados.

Pasta routes:
para as rotas do projeto;
nome padrão do arquivo: songRoutes.js;
criar arquivo index.js, quando mais de uma collection.

Pasta controllers:
para criar as funções com as requests e responses do projeto;
nome padrão do arquivo: songController.js;
importante:
1-) colocar o nome referência na função para melhor leitura assim: getAllSongs;
2-) tornar a função assíncrona com async/await sempre que tiver acesso a bando de dados;
3-) não é preciso importar o express, pois a manipulação é toda nas rotas, de onde essa função é chamada;
4-) na prática não se deve enviar a mensagem de erro para o front-end (message: err.message).

Pasta models:
para criar as funções de escrita e leitura do banco de dados;
nome padrão do arquivo: songModels.js;
opcionalmente o arquivo de configuração de acesso ao banco de dados pode ficar nesta pasta.