import unittest

from AlgoritmoGPS import Grafo


class TestUtils(unittest.TestCase):

    def test_grafo(self):
        diccionario = {0:"Ecuador",1:"Panamá",2:"Brasil",3:"EEUU",4:"Canadá",5:"Argentina",6:"Chile",7:"Perú",8:"Uruguay",9:"Paraguay",10:"Bolivia",11:"Venezuela",12:"Colombia",13:"México",14:"Costa Rica",15:"Francia",16:"Sudáfrica",17:"Rusia",18:"España",19:"China",20:"Japón"}

        g = Grafo(21,diccionario)
        g.añadir_locaciones(0,1,3)
        g.añadir_locaciones(0,12,2)
        g.añadir_locaciones(0,3,1)
        g.añadir_locaciones(0,7,2)
        g.añadir_locaciones(0,10)
        g.añadir_locaciones(0,6,1)
        g.añadir_locaciones(0,14,1)

        g.añadir_locaciones(1,15,1)

        g.añadir_locaciones(2,7,1)
        g.añadir_locaciones(2,16,2)

        g.añadir_locaciones(3,4,1)


        g.añadir_locaciones(4,17,1)
        g.añadir_locaciones(4, 19, 16)

        g.añadir_locaciones(5,6,2)

        g.añadir_locaciones(6,5,1)
        g.añadir_locaciones(6,10,5)

        g.añadir_locaciones(7,2,6)

        g.añadir_locaciones(8,0,2)
        g.añadir_locaciones(8,2,1)

        g.añadir_locaciones(9,10,2)
        g.añadir_locaciones(9,8,1)
        g.añadir_locaciones(9, 2, 10)

        g.añadir_locaciones(10,5,2)


        g.añadir_locaciones(11,18,2)

        g.añadir_locaciones(12,11,2)

        g.añadir_locaciones(13,3,2)
        g.añadir_locaciones(13,14,2)

        g.añadir_locaciones(14,7,1)
        g.añadir_locaciones(14, 3, 10)

        g.añadir_locaciones(15,0,2)

        g.añadir_locaciones(16,19,2)
        g.añadir_locaciones(16,20,2)

        g.añadir_locaciones(17, 4, 1)

        g.añadir_locaciones(18, 6, 5)
        g.añadir_locaciones(18,11,5)

        g.añadir_locaciones(19, 5, 2)
        g.añadir_locaciones(19, 20, 2)

        g.añadir_locaciones(20,19,2)
        g.añadir_locaciones(20,16,2)

        self.assertEqual(g.dfs(0,16,ruta = [], visitados = set()),['Ecuador', 'EEUU', 'Canadá', 'China', 'Japón', 'Sudáfrica'])
        

if __name__ == '__main__':
    unittest.main()
    