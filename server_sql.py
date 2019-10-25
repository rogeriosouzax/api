import pyodbc
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

# Criando a conexão com o banco de dados
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KNDBAK9\SQLEXPRESS;'
                      'Database=Lewis;'
                      'Trusted_Connection=yes;')

# Iniciando a applicação Flask
app = Flask(__name__)

# Criando uma API
api = Api(app)

# Criando a classe que ira conter os serviços da API herdando da classe Resource do modulo flask_restful
class Pessoas(Resource):
    
    def get(self):
        # Criando o cursor da conexão
        cursor = conn.cursor()
        # Executando a query desejada
        cursor.execute('SELECT * FROM [DBO].[PERSONS]')
        # Retornando os nomes das colunas da tabela
        columns = [description[0] for description in cursor.description]
        # Usando um list comprehension para criar um Dictionary com os dados retornados da consulta
        result = {'data': [dict(zip(tuple(columns) , row)) for row in cursor]}

        # Retornando o valor para web convertendo para JSON
        return jsonify(result)

class Car(Resource):
    
    def get(self, code):
        cursor = conn.cursor()
        # Selecionando os dados da tabela Cars passando um parametro para a clausula WHERE
        cursor.execute('SELECT * FROM dbo.Cars WHERE Id = %d ' %int(code))
        columns = [description[0] for description in cursor.description]
        result = {'data' : [dict(zip(tuple(columns) , row)) for row in cursor]}

        return jsonify(result)

class Cars(Resource):
    def get(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dbo.Cars')
        columns = [description[0] for description in cursor.description]
        result = {'data' : [dict(zip(tuple(columns), row)) for row in cursor]}

        return jsonify(result)

# Adicionando a minha API os recursos que estarão disponiveis para os usuários
api.add_resource(Pessoas, '/pessoas')
api.add_resource(Car, '/cars/<code>')
api.add_resource(Cars, '/cars')

if __name__ == '__main__':
    app.run(port=5000)
