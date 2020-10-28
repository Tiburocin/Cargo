from flask import Flask
from flask_restplus import Api, Resource, fields
from route_tienda import Tienda, TiendaById
from route_productos import Productos, ProductosById, CantidadProductos

app = Flask(__name__)
api = Api(app)

api.add_resource(Tienda,"/api/V01/tienda")
api.add_resource(Productos,"/api/V01/productos")
api.add_resource(TiendaById,"/api/V01/tienda/<int:id>")
api.add_resource(ProductosById,"/api/V01/productos/<int:sku>")
api.add_resource(CantidadProductos,"/api/V01/productos/cantidad/<int:sku>")

if __name__ == "__main__":
    app.run(debug = True)