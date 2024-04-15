from flask import Flask, jsonify, render_template, abort
app = Flask(__name__)

alunos = {
   1 : {'nome': 'Eduardo',
        'nota': [10,9.6,8]},
   2: {'nome': 'Bianca',
        'nota': [1,6,4]},
   3: {'nome': 'Carlos',
        'nota': [2,9.6,10]},
}


@app.route('/')
def hello():
    return render_template("index.html")
        
@app.route('/alunos')
def getAlunos():
    return jsonify(alunos)

@app.route('/alunos/<int:indice>')
def getAluno(indice):
    

    if indice in alunos.keys():
        return jsonify(alunos.get(indice))

    else:
        return jsonify("Pagina não encontrada", abort(404))


if __name__ == '__main__':
    app.run(debug=True)