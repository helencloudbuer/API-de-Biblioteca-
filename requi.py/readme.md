# Como utilizar! 

## Pré-requisitos

- Python 3 instalado
- Flask instalado (`pip install flask`)

## Passo a passo

1. Coloque o arquivo `app.py` em uma pasta no seu computador.

2. Abra o terminal nessa pasta e instale o Flask (caso ainda não tenha):
   ```bash
   pip install flask
   ```

3. Execute a aplicação:
   ```bash
   python app.py
   ```

4. O servidor vai iniciar em:
   ```
   http://127.0.0.1:5000
   ```

5. Use um navegador, Postman ou Thunder Client para testar as rotas abaixo.

## Rotas disponíveis

| Método | Rota            | Descrição                          |
|--------|-----------------|-------------------------------------|
| GET    | `/livro/<titulo>`| Consulta um livro pelo título      |
| GET    | `/autor?nome=`   | Consulta um autor pela query string |
| POST   | `/livro`         | Cadastra um novo livro              |

### Exemplo 1 — Consultar livro

```
GET http://127.0.0.1:5000/livro/Dom%20Casmurro
```

### Exemplo 2 — Consultar autor

```
GET http://127.0.0.1:5000/autor?nome=Machado%20de%20Assis
```

### Exemplo 3 — Cadastrar livro

```
POST http://127.0.0.1:5000/livro
Content-Type: application/json

{
  "titulo": "Grande Sertão: Veredas",
  "autor": "Guimarães Rosa",
  "ano": 1956
}
```

## Encerrar o servidor

No terminal onde o `app.py` está rodando, pressione `CTRL + C`.