# Ferramentas para Desenvolvimento Python

> O Pyton é um Ecossistema com muitas ferramentas e facilidades para o desenvolvedor.
> Uma forma do desenvolver aproveitar esse ambiente aumentando assim sua eficiência no desenvolvimento de algorítimos, é utilizar ferramentas que facilitem a gestão de todo ecosistema.
> Navegando nas "internets" da vida, pesquisando sobre o aprendizado de python encontrei algumas curiosidades, é comum ter conflitos de bibliotecas e versões do python na maquina local.
> Com o uso destas ferramentas também garantimos que o código ao ser compartilhado com outro dev, o mesmo terá facilmente instalado as dependencias necessárias acabando com o famoso na minha maquina não funciona.

## venv - Criação de Ambientes Virtuais

* [Documentação](https://docs.python.org/pt-br/3/library/venv.html)

#### Dentro da pasta do projeto verifique a versão do Python com pyenv

`$ pyenv version 3.10.2 (set by /home/heliezer/.pyenv/version)`

Estando dentro da pasta correta crie um virtual env com venv.

`$ python -m venv .venv`

E por fim acesse o ambiente virtual daquela pasta.

`$ source .venv/bin/activate`

Se tudo estiver correto o resultado será como no exemplo abaixo.
`(.venv) heliezer@hel:~/developer/study/python/python_training_basic$ `

O (.venv) indica que você está dentro do ambiente virtual e tudo o que for instalado aqui será refletido somente na pasta .venv/bin/activate.

## pyenv - Gerenciador de versões do Python na mesma maquina.

* [Instalação](https://github.com/pyenv/pyenv)
* [Comandos e Muitos Exemplos](https://realpython.com/intro-to-pyenv/#using-pyenv-to-install-pythonhttps:/)

## pipx - Instalar Programas e Executar programas de linhas de comandos sem conflitos.

* [Instalação](https://github.com/pypa/pipx)
* [Dicas e Comandos](https://pypa.github.io/pipx/)

## Poetry - Gerenciar Ambientes Projetos Python

* [Instalação](https://python-poetry.org/)
* [Dicas e Comandos](https://youtu.be/ZOSWdktsKf0)
* [Comandos Ativar Desativar Env no Poetry](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)

## ++ Referencias sobre o Tema.

* [Como Começar um Projeto Python Perfeito](https://blog.pronus.io/posts/python/como-comecar-um-projeto-python-perfeito/)
* [Como organizar um projeto Python? - Live de Python #192](https://youtu.be/O3bs4JtHrow)
* [Gerenciando Ambientes Virtuais Poetry e Pyenv](https://blog.pronus.io/posts/python/gerenciamento-de-versoes-ambiente-virtuais-e-dependencias-com-pyenv-e-poetry/)
