from flask import request
from flask_restplus import Resource, fields, Namespace
from model_productos import Productos_Model 
from db import Database

api = Namespace('user', description='user related operations')

bd = Database()

class Productos(Resource):

    def get(self):
        return bd.selectRows("select * from productos")
         
    @api.expect(Productos_Model.a_productos)
    def post(self):
        json_data = request.json
        nombre = json_data["nombre"]
        descripcion = json_data["descripcion"]
        cantidad = json_data["cantidad"]
        precio = json_data["precio"]
        id_Tienda = json_data["id_Tienda"]

        insert_query = "INSERT INTO productos (nombre, descripcion, cantidad, precio, id_Tienda) VALUES (%s,%s,%s,%s,%s)"
        record = (nombre, descripcion, cantidad, precio, id_Tienda)
        return bd.add(insert_query,record)

class ProductosById(Resource):

    def get(self,sku):
        return bd.selectRows("select * from productos where sku = {}".format(sku))

    def put(self,sku):
        return {'result' : 'Dulceria Id'}, 201

    def delete(self,sku):
        return {'result' : 'Dulceria Id'}, 201

class CantidadProductos(Resource):
    def get(self,sku):
        quantity = bd.getQuantity("select quantity from productos where sku = {}".format(sku))
        return quantity

