from flask import request, Response
from flask_restplus import Namespace, Resource, fields
from model_tienda import Tienda_Model
from db import Database

api = Namespace('user', description='user related operations')

bd = Database()

class Tienda(Resource):

    #Seleccion de todas las filas
    @api.route()
    def get(self):
        res = bd.selectRows("select * from tienda")
        return Response(res, mimetype="application/json", status=200)

    #Añade registro
    @api.expect(Tienda_Model.a_tienda)
    def post(self):
        json_data = request.json
        name = json_data["name"]
        direccion = json_data["direccion"]
        telefono = json_data["telefono"]

        insert_query = "INSERT INTO shop (name, direccion, telefono) VALUES (%s,%s,%s)"
        record = (name, direccion, telefono)
        res = bd.add(insert_query,record)
        return Response(res, mimetype="application/json", status=200)

#Busqueda por ID
class TiendaById(Resource):

    def get(self,id):
        res = bd.selectRows("select * from tienda where id_tienda = {}".format(id))
        return Response(res, mimetype="application/json", status=200)
