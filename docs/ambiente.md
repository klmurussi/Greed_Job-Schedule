## Instalação 

**Linguagem**: Python<br>

**Biblioteca**: pip3<br>

O projeto foi criado em um ambiente de desenvolvimento linux utilizando a IDE [VSCode](https://code.visualstudio.com/)

1. Inicialmente, caso não haja uma versão instalada, instale o [python3](https://www.python.org/downloads/)
2. Também é necessário utilizar o gerenciador de pacotes do python3 o [pip3](https://pypi.org/project/pip/#description)
3. Após obter o pip3, basta utilizar o pip3 pela linha de comando para obter a bilbioteca pythonds
  ```bash
  pip3 install pythonds
  ```
4. Caso esteja utilizando o VSCode, é interessante instalar as extensões [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) e [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Uso 

Para uso do projeto basta rodar o projeto a partir da pasta do projeto.
  ```bash
  python3 main.py
  ```
Ao utilizar esse metódo, basta seguir as requisições do terminal e registrar as requiridas atividades.
Para realizar o cadastro mais rapidamente, pode ser útil inicializar o programa com um arquivo de texto contendo as tarefas, o modelo do arquivo é mostrado abaixo.
  ```C
  Atividade1 //aqui se deve colocar o nome da atividade
  10 //aqui se deve colocar a hora do ínicio da atividade, não são aceitos horários decimais, apenas inteiros
  11 //horario final da atividade, apenas inteiros
  1 2 3//dias da semana que a atividade acontecerá, insira apenas espaços ou um numero de 1 a 7 nesse campo
  S //caso queira ou não adicionar outra ativida (S para sim, N para não)
  Atividade2
  12
  14
  2
  N
  ```
Para executar o código com auxílio do arquivo texto basta seguir esse exemplo. O exemplo acima está disponível no repositório como `test2.txt`
  ```bash
  python3 sources/main.py < seuarquivo.txt
  ```
Obs.: No repositório há os arquivos `test1.txt` e `test2.txt` previamente preenchidos como exemplo para teste