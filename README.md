# FindYourPet

## [SENAC] - Projeto Integrador -  DESENVOLVIMENTO DE SISTEMAS ORIENTADO A DISPOSITIVOS MÓVEIS E BASEADOS NA WEB

A segunda entrega do PI será mais desafiadora e vocês deverão utilizar os conhecimentos adquiridos em disciplinas de desenvolvimento web.

1) Pensem em uma história/jornada a partir da visão de produto, personas e protótipo desenvolvido na primeira entrega e elabore uma aplicação web que reflita este cenário/jornada.
2) Deve ser entregue o projeto desenvolvido postado no GitHub (enviar o link) com o README explicado com devemos testar a aplicação desenvolvida (instalações e visualização). O nome dos integrantes e o Grupo deve constar no README.
3) Produzir um vídeo de aproximadamente 1 min mostrando o app web em funcionamento. O vídeo pode ser postado na entrega ou também enviar um link privado do YouTube.


## Tecnologias 

As tecnologias utilizadas no projeto são:

* Python 3.10 (Linguagem de Programação)
* Flask 2.1.2 (Framework)
* Bootstrap 5.2 (Framework)
* SQLite 3.38.5 (Banco de Dados)
* HTML5 (Linguagem de Marcação)
* CSS3 (Linguagem de Estilo)


## Serviços Utilizados

* Github
* Azure (Web App)


## Pré-requisitos
* Instalação Python 3.10;
    - Ubuntu 20.04
        > sudo apt install python3.10
    - Windows 10
        - Download (https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)  e instale
* Instalação pip
    - Ubuntu 20.04
        > sudo apt install python3-pip
* Instalação python3-venv
    - Ubuntu 20.04
        > sudo apt install python3-venv
* Instalação git
    - Windows 10
        - Download (https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe) e instale


## Iniciando a Aplicação

* Para abaixar o repositório execute o comando abaixo.
    > git clone https://github.com/wferreirajr/FindYourPet_Flask.git
* Após baixar o repositório entre no diretório que foi criado, para isso execute o comando abaixo.
    > cd FindYourPet_Flask
* Agora precisamos instalar o nosso ambiente virtual para isolar este app, o comando abaixo nos ajuda com isso.
    > python3 -m venv .
* Para ver toda a estrutura podemos digital o comando
    - Ubuntu
        > ls -last
    - Windows
        > dir
* Para a ativação do nosso ambiente virtual devemos executar o comando abaixo.
    - Ubuntu
        > source ./bin/activate
    - Windows 
        > Scripts\activate.bat
* Agora vamos instalar todos os pré-requisitos que precisamos para a aplicação no nosso ambiente virtual, o comando que faz esta magia é:
    > pip install -r requirements.txt
* Agora é somente executar a aplicação com o comando abaixo:
    > flask run
* Agora podemos abrir o navegador e digitar o endereço http://127.0.0.1:5000/ para acesso a página principal da aplicação.
## Como Utilizar

* 1. Primeiro vamos fazer o cadastro de um animalzinho para doação, para fazermos este cadastro devemos abrir o endereço http://127.0.0.1:5000/admin
* 2. Para cadastrar o nosso animalzinho clique em Registro e em seguida em Cadastrar, agora preencha todos os campos inclusive a foto.
* 3. Após o cadastro podemos voltar na página principal no endereço http://127.0.0.1:5000/ e podemos clicar no link dos gatos ou cachorros, dependendo do cadastro que foi feito, e podemos ver que o nosso novo animalzinho já aparece na página principal.


## Funcionalidades

* Página Administração
    - Cadastro de usuários
    - Cadastro de aminais

* Página Principal
    - Registro de usuários
    - Lista dos cachorros para doação
    - Lista dos gatos para doação


## Links

* Página principal (http://127.0.0.1:5000)

* Página administrativa (http://127.0.0.1:5000/admin)


## Versões

1.0.0.0 (beta)


## Autores

* **Alex Ferreira Nunes** ID: 1142194784
* **Eduardo Felipe da Silva Kreve** ID: 1142515898
* **Erivaldo Herculano dos Santos** ID: 1140037707
* **Fabio Amorim de Lima** ID: 1140753327
* **Gabriel Guimarães** ID: 1142200182
* **Giordano Mendes Bueno** ID: 1142202174
* **Luana Fernanda Deoclecio** ID: 1141126529
* **Matheus Lima Barbosa** ID: 1142195493
* **Wilson Ferreira Junior** ID: 1142204645

Por favor, siga o github e junte-se a nós!

Obrigado por me visitar e boa codificação!

