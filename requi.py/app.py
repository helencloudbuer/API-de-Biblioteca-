from flask import Flask, request, jsonify 

app = Flask(__name__)


# "banco de dados" simples em memória, só para simular alguns livros :)
# já cadastrados para o Requisito 1 e 2 funcionarem com dados de exemplo!


livros = {
    "Dom Casmurro": "Machado de Assis",
    "O Cortiço": "Aluísio Azevedo",
    "Iracema": "José de Alencar",
}

# requisito 1 - consultar livros 
# GET /livro/<titulo> 

@app.route("/livro/<titulo>", methods=["GET"])
def consultar_livro(titulo):
    autor = livros.get(titulo)

    if autor is None: 
        return jsonify({"erro": "Livro não encontrado :/"}), 404 # erro 404

    return jsonify({
        "titulo": titulo,
        "autor": autor
    })


# requisito 2 - conlsutar autor (query string)
# GET /autor?nome=Machado%20de%20Assis

@app.route("/autor", methods=["GET"])
def consultar_autor(): 
    nome = request.args.get("nome")

    if not nome: 
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400 # errp 400 

    # verifica se algum livro tem esse autor 
    autor_encontrado = None 
    for titulo, autor in livros.items():
        if autor.lower() == nome.lower(): 
            autor_encontrado = autor 
            break

    if autor_encontrado is None: 
        return jsonify({"erro": "Autor não encontrado :/"}), 404 # erro 404 

    return jsonify({"autor": autor_encontrado})

# requisito 3 - cadastrar livro

@app.route("/livro", methods=["POST"])
def cadastrar_livros(): 
    dados = request.get_json()

    if not dados: 
        return jsonify({"erro": "Nenhum dado JSON foi enviado"}), 400 # erro 400

    titulo = dados.get("titulo")
    autor = dados.get("autor")
    ano = dados.get("ano")

    if not titulo or not autor or not ano: 
        return jsonify({"erro": "Titutlo, autor e são obrigatórios"}), 400 # erro 400 

    # vai salvar no "banco" em memória

    livros[autor] = titulo

     
    return jsonify({
        "mensagem": "livro cadastrado com sucesso! :)",
        "dados": {
            "titulo": titulo, 
            "autor": autor, 
            "ano": ano
        }
    }), 201 # erro 201 
if __name__ == "__main__":
    app.run(debug=True)