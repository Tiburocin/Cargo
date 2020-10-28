from flask_restplus import Namespace, fields

class Productos_Model():
    api = Namespace('user', description='user related operations')
    a_productos = api.model('Productos', 
    {'Nombre' : fields.String,
    'id_Tienda' : fields.Integer,
    'Descripcion' : fields.String,
    'Cantidad' : fields.Integer,
    'Precio' : fields.Float})
