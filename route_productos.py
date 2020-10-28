from flask import request, Response
from flask_restplus import Resource, fields, Namespace
from model_productos import Productos_Model 
from db import Database

api = Namespace('user', description='user related operations')

bd = Database()


class Productos(Resource):

    #Seleccion de toda las las filas
    def get(self):
        return bd.selectRows("select * from productos")
         
    #Añade registro
    @api.expect(Productos_Model.a_productos)
    def post(self):

        #Query Param
        nombre = request.args.get('nombre')
        descripcion = request.args.get('descripcion')
        cantidad = request.args.get('cantidad')
        precio = request.args.get('precio')
        id_Tienda = request.args['id_Tienda']

        #Json Param
        # json_data = request.json
        # nombre = json_data["nombre"]
        # descripcion = json_data["descripcion"]
        # cantidad = json_data["cantidad"]
        # precio = json_data["precio"]
        # id_Tienda = json_data["id_Tienda"]

        insert_query = "INSERT INTO productos (nombre, descripcion, cantidad, precio, id_Tienda) VALUES (%s,%s,%s,%s,%s)"
        record = (nombre, descripcion, cantidad, precio, id_Tienda)
        res = bd.add(insert_query,record)
        return Response(res, mimetype="application/json", status=200)

#Busqueda por ID
class ProductosById(Resource):

    def get(self,sku):
        res = bd.selectRows("select * from productos where sku = {}".format(sku))
        return Response(res, mimetype="application/json", status=200)

#Seleccion de la cantidad de producto
class CantidadProductos(Resource):
    def get(self,sku):
        res = bd.getQuantity("select quantity from productos where sku = {}".format(sku))
        return Response(res, mimetype="application/json", status=200)

