import unittest
from route_productos import Productos, ProductosById, CantidadProductos

class Test_Productos(unittest.TestCase):

    def setUp(self):
        self.productos = Productos()
        self.productosById = ProductosById()
        self.cantidad = CantidadProductos()

    def test_Get(self):
        self.assertTrue(self.productos.get())
        self.assertTrue(self.productosById.get(1))
        self.assertTrue(self.cantidad.get(1))


if __name__ == "__main__":
    unittest.main()