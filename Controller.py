from flask import Flask
from Model import Home
from Model_Aluno import Aluno


# Configs
app = Flask(__name__)


# Rotas
@app.route('/')
def home():
    return Home.tela_inicial()


@app.route('/aluno')
def alunoe():
    aluno1 = Aluno('Guilherme', 12345678910, 11987654321, 'guilherme@aluno.com')
    return aluno1.get_aluno_data()


# Main
if __name__ == '__main__':
    app.run(debug=True, port=5000)
