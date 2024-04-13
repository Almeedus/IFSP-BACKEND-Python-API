# API Flask Simple

Criação de API em Flask para a matéria de Backend I.

### 📋 Escopo do Projeto

API conta com a ideia de criar 5 rotas construídas em GET e POST além da rota principal("/"). A ideia do projeto desenvolvido é desenvolver o processo de consulta e inserção de dados em variaveis que contém alunos e as notas dos alunos.

A mensagem de retorno é um JSON com as seguintes informações:\
{\
  "nome": "Eduardo"; [STRING]\
  "notas": [8.0,9.5,10]; [FLOAT]\
  "media": media; [FLOAT]\
}

- [GET] / 
  Rota de saudáções ao sistema.
  
- [GET] alunos 
  Rota de alunos, retornará um JSON com todos os alunos cadastrados na variável.\
    Status 200: Retorna os dados dos alunos.\
    Status 404: Retorna uma mensagem de erro ao encontrar o aluno.
  
- [GET] alunos/index 
  Rota de alunos onde retorna um JSON de apenas um aluno que corresponde ao index passado.\
    Status 200: Retorna os dados do aluno.\
    Status 404: Retorna uma mensagem de erro ao encontrar o aluno.
  
- [POST] /alunos 
  Rota de inserção de dados referentes aos alunos. \
    Status 200: Retorna uma mensagem de inserção realizada com sucesso. \
    Status 409: Retorna uma mensagem de erro referente a conflito de index ao inserir o aluno. \
    Status 400: Retorna uma mensagem de erro referente a erros no corpo da requisição. \
  
- [POST] /notas 
  Rota de inserção de dados referentes aos notas. \
    Status 200: Retorna uma mensagem de inserção realizada com sucesso. \
    Status 409: Retorna uma mensagem de erro referente a conflito de index ao inserir o aluno. \
    Status 400: Retorna uma mensagem de erro referente a erros no corpo da requisição. \
  
### 📋 Pré-requisitos

Para a utilização deste projeto é necessário a linguagem e algumas bibliotecas selecionadas anteriormente:

```
Python 3.11
Flask 2.3.0
```

### 🔧 Instalação

Faça o clone deste projeto: 

```
git clone https://github.com/Almeedus/api-flask-simple.git
```

Dentro do diretório abra o terminal e instale as bibliotecas que estão dentro do requirements.txt:

```
pip install -r requirements.txt
```
Caso não funcione utilize o seguinte comando:
```
pip3 install -r requirements.txt
```

## ⚙️ Executando os testes

Rode o projeto e abra sua ferramenta de consumo de API (Insomina, Postman, Curl, etc) e configure as rotas.

### 🔩 Rotas

- [GET] / 
  - Configure o método como GET e insira a rota "/".
  
- [GET] /alunos 
  - Configure o método como GET e insira a rota "/alunos".
    
- [GET] /alunos/index 
  - Configure o método como GET e insira a rota "/alunos/index".
    
- [POST] /alunos 
  - Configure o método como POST e insira a rota "/alunos".
  - Utilize uma requisição de body:\
    - { \
        "index": 1;\
        "nome": "Eduardo";\
      }
- [POST] /notas 
  - Configure o método como POST e insira a rota "/notas".
  - Utilize uma requisição de body:\
    - { \
        "index": 1;\
        "notas": [8.0, 9.5, 10]\
      }
      

## 🛠️ Construído com

* [Python 3.11](https://docs.python.org/3.11/) - Linguagem base utilizada;
* [Flask 2.3.0](https://flask.palletsprojects.com/en/3.0.x/) - Framework de criação de rotas.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺.
