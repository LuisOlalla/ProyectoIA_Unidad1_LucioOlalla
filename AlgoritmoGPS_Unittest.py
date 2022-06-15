#Importar módulo unittest
import unittest
#Importar del módulo AlgoritmoGPS el Grafo y el procedimiento ubicaciones
from AlgoritmoGPS import Grafo, ubicaciones

#Clase TestUbicaciones
class TestUtils(unittest.TestCase):
    '''
    Definicion de la clase TestUtils
    Este método permite realizar el test para el módulo importado
    '''
    def test_grafo(self):
        '''
        Funcion que permite realizar el test para el grafo
        Parametros:
            self:
                Objeto que contiene los atributos de la clase
        Retorna:
            Nada
        '''
        #Definición del diccionario de ubicaciones
        diccionario = {0:"Ecuador",1:"Panamá",2:"Brasil",3:"EEUU",4:"Canadá",5:"Argentina",6:"Chile",7:"Perú",8:"Uruguay",9:"Paraguay",10:"Bolivia",11:"Venezuela",12:"Colombia",13:"México",14:"Costa Rica",15:"Francia",16:"Sudáfrica",17:"Rusia",18:"España",19:"China",20:"Japón"}
        #Definición del grafo
        g = Grafo(21,diccionario)
        #Llamar al procedimiento ubicaciones para ingresar los nodos en el grafo
        ubicaciones(g)
        #Llamar al procedimiento dfs para realizar el recorrido del grafo y obtener la ruta
        self.assertEqual(g.dfs(0,16, ruta=[],visitado=set()),['Ecuador', 'EEUU', 'Canadá', 'China', 'Japón', 'Sudáfrica'])
        #Llamar al procedimiento dfs para determinar si el numero de nodos es correcto
        self.assertFalse(g.dfs(0,22, ruta=[],visitado=set()))
        #Llamar al procedimiento dfs para determinar si el numero de nodos es correcto
        self.assertTrue(g.dfs(0,1))

#Definición del método main para ejecutar las pruebas
if __name__ == '__main__':
    #Se ejecuta el test
    unittest.main()
    