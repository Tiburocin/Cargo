from flask import request
from flask_restplus import Namespace, Resource, fields
from model_tienda import Tienda_Model
from db import Database

api = Namespace('user', description='user related operations')

bd = Database()

class Tienda(Resource):

    @api.marshal_with(Tienda_Model.a_tienda, envelope='resource')
    def get(self):
        return bd.selectRows("select * from tienda")

    @api.expect(Tienda_Model.a_tienda)
    def post(self):
        json_data = request.json
        name = json_data["name"]
        direccion = json_data["direccion"]
        telefono = json_data["telefono"]

        insert_query = "INSERT INTO shop (name, direccion, telefono) VALUES (%s,%s,%s)"
        record = (name, direccion, telefono)
        return bd.add(insert_query,record)

class TiendaById(Resource):

    def get(self,id):
        return bd.selectRows("select * from tienda where id_tienda = {}".format(id))

    def put(self,id):
        return {'result' : 'Tienda Id'}, 201

    def delete(self,id):
        return {'result' : 'Tienda Id'}, 201
