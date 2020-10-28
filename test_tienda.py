import unittest
import json
from route_tienda import Tienda, TiendaById

class Test_Productos(unittest.TestCase):

    def setUp(self):
        self.tienda = Tienda()
        self.tiendaById = TiendaById()



    def test_Get(self):
        self.assertTrue(self.tienda.get())
        self.assertTrue(self.tiendaById.get(1))


if __name__ == "__main__":
    unittest.main()