import unittest

from AlgoritmoGPS import Grafo, ubicaciones


class TestUtils(unittest.TestCase):

    def test_grafo(self):
        diccionario = {0:"Ecuador",1:"Panamá",2:"Brasil",3:"EEUU",4:"Canadá",5:"Argentina",6:"Chile",7:"Perú",8:"Uruguay",9:"Paraguay",10:"Bolivia",11:"Venezuela",12:"Colombia",13:"México",14:"Costa Rica",15:"Francia",16:"Sudáfrica",17:"Rusia",18:"España",19:"China",20:"Japón"}

        g = Grafo(21,diccionario)
        ubicaciones(g)

        self.assertFalse(g.dfs(0,16),['Ecuador', 'EEUU', 'Canadá', 'China', 'Japón', 'Sudáfrica'])
        

if __name__ == '__main__':
    unittest.main()
    