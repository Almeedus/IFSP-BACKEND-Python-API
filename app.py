from flask import Flask, jsonify, render_template, abort, request
app = Flask(__name__)

alunos = {
   "1" : {'nome': 'Eduardo',
        'nota': [10,9.6,8]},
   "2": {'nome': 'Bianca',
        'nota': [1,6,4]},
   "3" : {'nome': 'Carlos',
        'nota': [2,9.6,10]},
}


@app.route('/')
def hello():
    return render_template("index.html")
        
@app.route('/alunos')
def getAlunos():
    return jsonify(alunos),200

@app.route('/alunos/<int:indice>')
def getAluno(indice):
    if indice in alunos.keys():
        return jsonify(alunos.get(indice)),200

    else:
        return jsonify("Pagina não encontrada", abort(404))

@app.route('/alunos', methods=['POST'])
def postAluno():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Nenhum JSON encontrado no corpo da requisição'}), 400
    
    indice = data.get('indice')
    nome = data.get('nome')

    if indice is None or nome is None:
        return jsonify({'error': 'Índice e nome são campos obrigatórios'}), 400

    if indice in alunos:
        return jsonify({'error': 'Dados não podem ser inseridos, índice existente'}), 409
    
    else:
        alunos[indice] = {'nome': nome, 'nota': []}
        return jsonify({'message': 'Dados inseridos com sucesso'}), 200
    
@app.route('/notas', methods=['POST'])
def postNotas():
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Nenhum JSON encontrado no corpo da requisição'}), 400
    
    indice = data.get('indice')
    nota = data.get('nota')

    if indice is None or nota is None:
        return jsonify({'error': 'Índice e notas são campos obrigatórios'}), 400

    if indice in alunos:
        alunos[indice]['nota'].append(nota)
        return jsonify({'message': 'Dados inseridos com sucesso'}), 200
        
    else:
        return jsonify({'error': 'Dados não podem ser inseridos, índice existente'}), 409

if __name__ == '__main__':
    app.run(debug=True)