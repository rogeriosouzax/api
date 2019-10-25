from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)

api = Api(app)

class Itens(Resource):
    def get(self):
        itens = pd.read_csv('itens_loja.csv')
        lista_itens = []
        
        for index, row in itens.iterrows():
            lista_itens.append({'Codigo' : row['Codigo'], 'Descricao' : row['Descricao'], 'Quantidade' : row['Quantidade'], 'Valor' : row['Valor']})
        
        dados = {'data' : lista_itens}

        return jsonify(dados)
        
api.add_resource(Itens, '/itens')

if __name__ == '__main__':
    app.run()