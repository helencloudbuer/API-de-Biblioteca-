# API de Biblioteca

API REST simples desenvolvida em Python com Flask para simular um sistema de consulta e cadastro de livros em uma biblioteca.

## Funcionalidades

- **Consultar livro por título** — `GET /livro/<titulo>`
- **Consultar autor por Query String** — `GET /autor?nome=...`
- **Cadastrar novo livro** — `POST /livro`

## Tecnologias

- Python 3
- Flask

## Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Instale as dependências
pip install flask
```

## Como executar

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000`

## Endpoints

### 1. Consultar Livro

```
GET /livro/<titulo>
```

**Exemplo:**
```
GET http://127.0.0.1:5000/livro/Dom%20Casmurro
```

**Resposta:**
```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis"
}
```

### 2. Consultar Autor

```
GET /autor?nome=<nome_do_autor>
```

**Exemplo:**
```
GET http://127.0.0.1:5000/autor?nome=Machado%20de%20Assis
```

**Resposta:**
```json
{
  "autor": "Machado de Assis"
}
```

### 3. Cadastrar Livro

```
POST /livro
```

**Body (JSON):**
```json
{
  "titulo": "Grande Sertão: Veredas",
  "autor": "Guimarães Rosa",
  "ano": 1956
}
```

**Resposta:**
```json
{
  "mensagem": "Livro cadastrado com sucesso!",
  "dados": {
    "titulo": "Grande Sertão: Veredas",
    "autor": "Guimarães Rosa",
    "ano": 1956
  }
}
```

## Testando a API

Recomenda-se o uso de ferramentas como [Postman](https://www.postman.com/) ou a extensão [Thunder Client](https://www.thunderclient.com/) (VS Code) para testar as rotas.

## Observações

Nesta versão, os dados são armazenados apenas em memória (não há banco de dados), portanto as informações são perdidas ao reiniciar o servidor.
