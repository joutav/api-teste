from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from analisador_frases import polaridade_sentimento
import pickle

modelo = pickle.load(open('modelos/modelo.sav', 'rb'))


colunas = ['tamanho', 'ano', 'garagem']


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'jao'
app.config['BASIC_AUTH_PASSWORD'] = '123'

basic_auth = BasicAuth(app)


@app.route('/')
def home():
    return 'Minha primeira API'


if __name__ == '__main__':
    app.run()


@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    polaridade = polaridade_sentimento(frase)
    return f'polaridade: {polaridade}'


@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    valor = modelo.predict([dados_input])
    return jsonify(preco=valor[0])