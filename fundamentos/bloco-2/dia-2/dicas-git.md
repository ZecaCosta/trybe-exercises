# GIT

## O que é Git?
Git é um sistema de controle de versão de arquivos. Através deles podemos desenvolver projetos na qual diversas pessoas podem contribuir simultaneamente no mesmo, editando e criando novos arquivos e permitindo que os mesmos possam existir sem o risco de suas alterações serem sobrescritas

## O que é Github?
O Github é um serviço web que oferece diversas funcionalidades extras aplicadas ao git, tais como: projeto ágil de sw, controle de issues, Kanban, Pull Request e Code Review.

## Git/Github
Formam um sistema distribuído e descentralizado de controle de versões (DVCS). No caso o Git é um repositório local e Github o repositório remoto. Trabalham com três conceitos básicos: Ramificação (branch), mesclagem (merge) e resolução de conflitos.

## O que significa ser descentralizado?
Diferente dos sistemas cliente-servidor, quando cabe ao servidor controlar as versões, no sistema descentralizado as versões são estanques (independentes) e assíncronas (não sincronizadas automaticamente), ou seja, cada máquina controla tem sua própria versão e quando for o caso “empurra”  (push) sua versão para o repositório remoto, que após aprovação é “mesclada” (merge) a versão oficial.

## O que significa controle de versões?
O sistema gerencia diferentes versões através de processo de ramificação (branches) e commits (pacote de alterações) que permite em casos de necessidade retornar uma versão anterior.

## Por que um controle de versões?
- Manter um histórico de desenvolvimento;
- Desenvolvimento paralelo;
- Customização da versão em produção;
- Inclusão de novas features;
- Alterações de layout (design).

## Configuração
As configurações do GIT são armazenadas no arquivo **.gitconfig** localizado dentro do diretório do usuário do Sistema Operacional.

As configurações realizadas através dos comandos abaixo serão incluídas no arquivo citado acima.

### Setar usuário
	git config --global user.name "Zeca Costa"

### Setar email
	git config --global user.email jccostaso@gmail.com

### Listar configurações
	git config --list

### Ignorar Arquivos

Os nomes de arquivos/diretórios ou extensões de arquivos listados no arquivo **.gitignore** não serão adicionados em um repositório. Existem dois arquivos .gitignore, são eles:

* Geral: Normalmente armazenado no diretório do usuário do Sistema Operacional. O arquivo que possui a lista dos arquivos/diretórios a serem ignorados por **todos os repositórios** deverá ser declarado conforme citado abaixo. O arquivo não precisa ter o nome de **.gitignore**.

	git config --global core.excludesfile ~/.gitignore

* Por repositório: Deve ser armazenado no diretório do repositório e deve conter a lista dos arquivos/diretórios que devem ser ignorados apenas para o repositório específico. O arquivo precisa ter o nome de **.gitignore**

## Processo de versionamento
Considerando que controlar as alterações é extremamente importante, podemos concluir que é uma boa prática gerar inúmeras versões durante todo processo de alteração. Na prática, a cada alteração ou patch (conjunto de pequenas alterações), devemos gerar uma nova versão destas alterações.

### Status
Antes do processo em si, será importante esclarecer os estágios (status) que um arquivo pode estar durante o processo, conforme a seguir:

- Modificado (Untracked/Modified): arquivo em sua forma original ou depois de sofrer uma alteração;
- Adicionado ou preparado (Index/Stage): arquivo após ter sido adicionado;
- Comitado ou consolidado (Committed): arquivo após ter sido comitado.

### Verificar status dos arquivos/diretórios

	git status

Em caso de dúvida, é sempre uma boa ideia executar o comando `git status`. O comando git status mostra apenas informações, ele não modifica commits nem causa mudanças no repositório local.

Um recurso útil do status do git é que ele fornecerá informações úteis dependendo da sua situação atual. Em geral, podemos contar com ele para lhe dizer:

- Para onde HEAD está apontando, seja uma branch ou um commit;

- Se temos algum arquivo modificado no diretório atual que ainda não tenha sido submetido;

- Se os arquivos alterados são preparados (staged) ou não;

- Se a branch local atual está conectada a uma branch remota, então git status irá dizer se a branch local está atrasada ou adiantada por qualquer commit;

- Durante os conflitos de mesclagem, o git status também informará exatamente quais arquivos são a origem do conflito.

## Ajuda

### Geral
	git help
	
### Comando específico
	git help add
	git help commit
	git help <qualquer_comando_git>
	
## Inicializando um repositório Git:
Um repositório Git pode ser inicializado de duas formas:

- A partir de um repositório remoto já existente, por exemplo, do Github;
- Criar um novo repositório local (git init).

### A partir de um repositório remoto
Essa é a forma mais usual, um repositório remoto disponível no Github pode ser “baixado” para uma máquina local. Esse processo de baixar do repositório remoto (Github) é como se fosse um processo de `clonagem` da versão original, ou seja, uma cópia idêntica é criada no repositório local (máquina local) para que a partir desta cópia possamos alterar o que for necessário, sem qualquer vínculo automático com a versão original armazenada no repositório remoto (Github).

### Criar novo repositório local

	git init

### Excluir repositório local
Para excluir um repositório local, basta simplesmente excluir a pasta `.git`, conforme comando abaixo:

	rm -rf .git

**Nota:**
Ao se apagar a pasta .git, todo o histórico de commits será perdido.

### Procedimento completo sugerido pelo Github, para se criar um novo repositório local

- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/ZecaCosta/teste.git
- git push -u origin main

## Adicionar arquivo/diretório (staged area)
Adicionar as alterações untracked (arquivos novos e alterados) na área em que ficarão disponíveis para commit (changes to be commited) conhecida com index ou stage area:

### Adicionar um arquivo em específico

	git add meu_arquivo.txt

### Adicionar um diretório em específico

	git add meu_diretorio

### Adicionar todos os arquivos/diretórios
	
	git add .	
	
### Adicionar um arquivo que esta listado no .gitignore (geral ou do repositório)
	
	git add -f arquivo_no_gitignore.txt

## Remover arquivo (staged area)
É possível desfazer uma adição realizada e retornar para o status Untracked/Modified.

### Desfazendo alteração local (working directory)
Este comando deve ser utilizando enquanto o arquivo não foi adicionado na **staged area**. 

	git checkout -- meu_arquivo.txt

### Remover um arquivo em específico

	git reset -- meu_arquivo.txt

### remover todos os arquivos
	
	git reset

## Comitar arquivo/diretório
Realizar um commit das alterações adicionadas. Realizar um commit é como se fosse tirada uma fotografia daquele exato momento.

git commit –m “mensagem que reflita exatamente o que está sendo atualizado”

**Notas:**
- A mensagem deve reflitir exatamente o que está sendo atualizado;
- Quando a mensagem de um comando commit está muito grande, normalmente é porque estamos demorando pra fazer commits, a boa prática pede que façamos small commits;

### Comitar um arquivo
	
	git commit meu_arquivo.txt
  git commit meu_arquivo.txt -m "mensagem de commit"

### Comitar vários arquivos

	git commit meu_arquivo.txt meu_outro_arquivo.txt
	
### Comitar todos os arquivos adicionados (staged)

	git commit -m "mensagem de commit"

**Nota:**
É possível realizar a adição e o commit num único comando, desde que sejam apenas alterações em arquivos e não criação de arquivos novos, conforme abaixo:

	git commit -am "mensagem de commit"

### Alterando mensagens de commit

	git commit --amend -m "Minha nova mensagem"

## Remover arquivo/diretório

### Remover arquivo

	git rm meu_arquivo.txt

### Remover diretório

	git rm -r diretorio

## Visualizar histórico

### Exibir histórico
Verifique os commits realizados através do comando:

	git log

**Nota:**
Os detalhes de um commit podem ser verificados através do comando:

	git show (default: apresenta o último commit realizado)

	git show <hash> pra um commit específico.

### Exibir histórico com diff das duas últimas alterações

	git log -p -2
	
### Exibir resumo do histórico (hash completa, autor, data, comentário e qtde de alterações (+/-))

	git log --stat
	
### Exibir informações resumidas em uma linha (hash completa e comentário)

	git log --pretty=oneline

## Gerenciar repositórios remotos

### Clonar um repositório remoto já existente
Usando-se SSH:
`git clone git@github.com:ZecaCosta/trybe-exercicios.git`

Usando-se HTTPS:
`git clone https://github.com/ZecaCosta/trybe-exercicios.git`

**Notas:** 
- O nome da pasta local criada será: `trybe-exercicios`;
- Todas as branches do repositório remoto clonado estarão disponíveis para serem acessadas localmente;
- Não é recomendável realizar as alterações na branch principal (main), pois nesta se encontra normalmente a versão que será colocada em produção ou mesmo que já está se encontra em produção.

### Exibir os repositórios remotos
Este comando mostra o nome do remote. Por padrão quando clonamos um repositório do GitHub, o nome do remote será `origin`, que é o alias da URL do repositório colonado
	
	git remote

Para consulta os remotes existentes, usamos o comando a seguir:

	git remote -v

**Nota:**
Caso a colonagem tenha sido feita usando-se o SSH, a URL será:

`origin  git@github.com:ZecaCosta/trybe-exercicios.git (fetch)`

 `origin  git@github.com:ZecaCosta/trybe-exercicios.git (push)`

Já a colonagem tenha sido com HTTPS, a URL será:

`origin  https://github.com/ZecaCosta/trybe-exercicios.git (fetch)`

`origin  https://github.com/ZecaCosta/trybe-exercicios.git (push)`

### Alterar a URL de um repositório remoto
O comando abaixo altera a URL de um repositório remoto existente.

	git remote set-url

Por exemplo, alterar a URL do remote de SSH para HTTPS:

`git remote set-url origin https://github.com/ZecaCosta/trybe-exercicios.git`

### Vincular repositório local com um repositório remoto
Caso precisemos vincular um repositório local a um repositório remoto já existente, devemos adicionar um novo remoto. Para isso devemos usar o comando adicionar remoto do git no terminal do diretório no qual o repositório local está armazenado.

O comando `git remote add` usa dois argumentos:

- Um nome de remote, por exemplo, origin
- Uma URL remota, por exemplo, `https://github.com/ZecaCosta/trybe-exercicios.git`

O comando ficará como a seguir:
 
`git remote add origin https://github.com/ZecaCosta/trybe-exercicios.git`

### Procedimento sugerido pelo Github para "empurrar" (push) um repositório local, a partir de uma linha de comando

- git remote add origin https://github.com/ZecaCosta/teste.git
- git branch -M main
- git push -u origin main

**Nota:**
Ao criar um repositório remoto no Github para importar um repositório local, pular o passo inicial de criar um arquivo, conforme mensagem a seguir:

	Initialize this repository with:
	Skip this step if you’re importing an existing repository.

### Renomear um repositório remoto 
Use o comando renomear o remoto do git para renomear um remoto existente.

O comando `git remote rename` tem dois argumentos:

- O nome de um remote existente, por exemplo origin
- Um novo nome para o remote, como trybe-exercicios

O comando ficará como a seguir:

	git remote rename origin trybe-exercicios
	
### Desvincular um repositório remoto
Use o comando `git remote rm` para remover uma URL remota do seu repositório.

O comando git remote rm tem um argumento:

- O nome de um remote, por exemplo, teste

O comando ficará como a seguir:

	git remote rm teste

**Nota:** o comando `git remote rm` não exclui o repositório do remote no servidor. Ele simplesmente remove o remote e suas referências do repositório local.

### Enviar arquivos/diretórios para o repositório remoto

O primeiro **push** de um repositório deve conter o nome do repositório remoto e a branch.

	git push -u origin main
	
Os demais **pushes** não precisam dessa informação

	git push
	
## Atualizar repositório local de acordo com o repositório remoto

### Exibir as branches no repositório local

	git branch -a

### Limpar as referências locais para branches remotas

O comando abaixo exibe as branches remotas que podem ser apagadas do repositório local:

	git remote prune origin --dry-run

Para efetivamente apagar usamos o comando abaixo:

	git remote prune origin

### Exibir informações dos repositórios remotos

	git remote show origin

### Atualizar os arquivos no branch atual

	git pull
	
### Buscar as alterações, mas não aplica-las no branch atual

	git fetch

## Branches

A **main** é a branch principal do GIT.

O **HEAD** é um ponteiro *especial* que indica qual é a branch atual. Por padrão, o **HEAD** aponta para a branch principal, a **main**.

### Criando uma nova branch

	git branch 2-1

### Trocando para um branch existente

	git checkout 2-1

	Neste caso, o ponteiro principal **HEAD** esta apontando para a branch chamada 2-1.

### Criando uma nova branch e já trocando 

	git checkout -b 2-1
	
	Neste caso, o ponteiro principal **HEAD** esta apontando para a branch chamada 2-1.
	
### Voltar para a branch principal (main)

	git checkout main
	
### Resolver merge entre as branches

	git merge 2-1
	
Para realizar o *merge*, é necessário estar na branch que deverá receber as alterações. O *merge* pode ser automático ou manual. O merge automático será feito em arquivos textos que não sofreram alterações nas mesmas linhas, já o merge manual será feito em arquivos textos que sofreram alterações nas mesmas linhas.

A mensagem indicando um *merge* manual será:

	Automerging meu_arquivo.txt
	CONFLICT (content): Merge conflict in meu_arquivo.txt
	Automatic merge failed; fix conflicts and then commit the result.

### Apagando uma branch

	git branch -d 2-1

A opção -d vai apagar a branch somente se já tiver sido feito o push e merge com a branch remota. Caso ainda isso não tenha ocorrido usar a opção - D para forçar que a branch seja apagada.

	git branch -D 2-1

### Listar branches

	git branch

### Listar branches com informações dos últimos commits

	git branch -v

### Listar branches que já foram mescladas (merged) com o **main**

	git branch --merged

### Listar branches que não foram mescladas (merged) com o **main**

	git branch --no-merged

### Criando branches no repositório remoto

### Criando uma branch remota com o mesmo nome

	git push origin 2-1

### Criando uma branch remota com nome diferente

	git push origin 2-1:2-2

### Baixar uma branch remota para edição

	git checkout -b 2-2 origin/2-2

### Apagar uma branch remota

	git push origin -d 2-2

## Glossário
* push = empurrar
* merge = juntar/mesclar/mesclagem
* download = baixado
* clone = clonagem/cópia exata
* commit = como a tradução em português não ajuda (comprometimento), na pratica adota-se a palavra em inglês.
* issues = versões
* deploy = transferir arquivo pra outro ambiente 
* feature = funcionalidade
* untracked = alteração não adicionada
* patch = "remendo", atualização ou correção
