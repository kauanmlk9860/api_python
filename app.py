#########################################################################################
 # Objetivo: Realizar uma api co python, com teste no postman
 # Data: 12/12/2025
 # Autor: Kauan Rodrigues 
 # Versões: 1.0

# URL Base - localhost
# End Point -
# localhost/livros(GET)
# localhost/livros(POST)
# localhost/livros/id (GET)
# localhost/livros/id (PUT)
# localhost/livros/id (DELETE)

# Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'Hábitos Atômicos',
        'autor': 'James Clear'
    }
]

# Consultar todos os livros 
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Criar novo livro 
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Editar Livro por ID 
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Excluir livro por id 
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)