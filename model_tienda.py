from flask_restplus import Namespace, fields

class Tienda_Model():
    api = Namespace('user', description='user related operations')
    a_tienda = api.model('Tienda', 
    {'Nombre' : fields.String,
    'Direccion' : fields.String,
    'Telefono' : fields.String})