'''
Implementación del algoritmo de busqueda BFS para generar la simulación de un GPS
La orientación se basa en la planificación de un viaje para encontrar lugares cercanos 
de interés por medio de un método de busqueda. 
'''
#Importamos la clase queue para la generación de Colas
from queue import Queue

'''
Generar la clase grafo que permite instanciar el objeto y definir
los nodos a considerar para obtener la búsqueda deseada
'''
class Grafo():
    
    def __init__(self, numero_de_nodos,diccionario,dirigido=True):
        '''
        Generar el constructor, este método permite instanciar el objeto creado
            Parámetros:
                numero_de_nodos : int
                    Determina el rango que tendra el grafo
                diccionario : set()
                    Genera una lista de los nodos que van a ser visitados
                dirigido : boolean
                    Determina si el grafo es dirigido o no
            Retorna:
                Nada
        Generar un control de excepciones
         try:
            except:
                print("Error")
        '''
        try:
            #Asignamos valores al número de nodos mediante el parámetro que se recibio
            self.m_numero_nodos = numero_de_nodos
            #Se genera el rango de nodos en base a m_numero_nodos
            self.m_nodos = range(self.m_numero_nodos)
            #Determinar si el grafo es dirigido o no dirigido
            self.m_dirigido = dirigido
            #Se genera un diccionario con los nodos que se van a visitar
            self.m_locaciones = diccionario
            #Se genera una lista de los nodos que se van a visitar
            self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
        except Exception as e:
            print(e)
    
    def añadir_locaciones(self,nodo1,nodo2,peso=1):
        '''
        Generar el método para añadir nodos al grafo
        Parámetros:
            nodo1 : int
                Nodo que se va a añadir
            nodo2 : int
                Nodo que se va a añadir
            peso : int
                Peso que se le asigna al nodo
        Retorna:
            Nada
        
        Generar un control de excepciones
        try:
            except:
                print("Error")
        '''
        try:
            #Se añade el nodo 1 al nodo 2
            self.m_lista_adyacencia[nodo1].add((nodo2,peso))
            #Se añade el nodo 2 al nodo 1
            if not self.m_dirigido:
                self.m_lista_adyacencia[nodo2].add((nodo1,peso))
        except Exception as e:
            print(e)
    def mostrar_lista_adyacencia(self):
        '''
        Generar el método para obtener los nodos adyacentes a un nodo
        Parámetros:
            Nada
        Retorna:
            Nada
        '''
        try:
            for clave in self.m_lista_adyacencia.keys():
                print("Nodo ", clave, ":", self.m_lista_adyacencia[clave])
        except Exception as e:
            print(e)
    
    
    def dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        """
        El método DFS permitirá imprimir el recorrdio generado mediant un nodo inicial y un nodo objetivo o final.
        A su vez, generará los nodos que fueron visitados y el recorrido que se tomo para llegar hacia ese
        nodo objetivo.
        """
        try:
            peso1=0
            # Se agrega el nodo inicial a la lista de visitados
            visitado.add(inicio)
            # Se agrega el nodo inicial a la lista de ruta
            ruta.append(diccionario[inicio])
        except Exception as e:
            print(e)
        
        try:
            # Si el nodo inicial es el objetivo se imprime el recorrido
            if inicio == objetivo:
                print("Recorrido: ", ruta)
                return ruta

            # Se recorre la lista de adyacencia del nodo inicial
            for(vecino, peso) in self.m_lista_adyacencia[inicio]:
                # Si el nodo vecino no ha sido visitado se llama al metodo dfs con el nodo vecino como inicio
                if vecino not in visitado:
                    #se asigna a la variable resultado el nodo vecino, el objetivo, la ruta y la lista de nodos visitados
                    resultado = self.dfs(vecino, objetivo, ruta, visitado) 
                    # Si el resultado no es nulo se retorna el resultado
                    if resultado is not None:
                        #Retorna resultado
                        return resultado 

        except Exception as e:
            print(e)

        try:
            # Si el resultado es nulo se retorna None        
            ruta.pop() 
            return None
        except Exception as e:
            print(e)
            
    def ubicaciones(grafo):

        grafo.añadir_locaciones(0,1,3)
        grafo.añadir_locaciones(0,12,2)
        grafo.añadir_locaciones(0,3,1)
        grafo.añadir_locaciones(0,7,2)
        grafo.añadir_locaciones(0,10)
        grafo.añadir_locaciones(0,6,1)
        grafo.añadir_locaciones(0,14,1)

        grafo.añadir_locaciones(1,15,1)

        grafo.añadir_locaciones(2,7,1)
        grafo.añadir_locaciones(2,16,2)

        grafo.añadir_locaciones(3,4,1)


        grafo.añadir_locaciones(4,17,1)
        grafo.añadir_locaciones(4, 19, 16)

        grafo.añadir_locaciones(5,6,2)

        grafo.añadir_locaciones(6,5,1)
        grafo.añadir_locaciones(6,10,5)

        grafo.añadir_locaciones(7,2,6)

        grafo.añadir_locaciones(8,0,2)
        grafo.añadir_locaciones(8,2,1)

        grafo.añadir_locaciones(9,10,2)
        grafo.añadir_locaciones(9,8,1)
        grafo.añadir_locaciones(9, 2, 10)

        grafo.añadir_locaciones(10,5,2)


        grafo.añadir_locaciones(11,18,2)

        grafo.añadir_locaciones(12,11,2)

        grafo.añadir_locaciones(13,3,2)
        grafo.añadir_locaciones(13,14,2)

        grafo.añadir_locaciones(14,7,1)
        grafo.añadir_locaciones(14, 3, 10)

        grafo.añadir_locaciones(15,0,2)

        grafo.añadir_locaciones(16,19,2)
        grafo.añadir_locaciones(16,20,2)

        grafo.añadir_locaciones(17, 4, 1)

        grafo.añadir_locaciones(18, 6, 5)
        grafo.añadir_locaciones(18,11,5)

        grafo.añadir_locaciones(19, 5, 2)
        grafo.añadir_locaciones(19, 20, 2)

        grafo.añadir_locaciones(20,19,2)
        grafo.añadir_locaciones(20,16,2)



if __name__ == "__main__":
    #Se crea un diccionario con los nodos que se van a visitar
    diccionario = {0:"Ecuador",1:"Panamá",2:"Brasil",3:"EEUU",4:"Canadá",5:"Argentina",6:"Chile",7:"Perú",8:"Uruguay",9:"Paraguay",10:"Bolivia",11:"Venezuela",12:"Colombia",13:"México",14:"Costa Rica",15:"Francia",16:"Sudáfrica",17:"Rusia",18:"España",19:"China",20:"Japón"}
    #Se crea un grafo dirigido 
    grafo = Grafo(21,diccionario)
   
    #Se llama al metodo ubicaciones
    grafo.ubicaciones()


    #Se muestra la lista de adyacencia
    grafo.mostrar_lista_adyacencia()

    #Implementación de dfs
    ruta_transversal1 = [] # Se inicializa la variable ruta_transversal
    ruta_transversal1 = grafo.dfs(0, 16) # Se almacena el recorrido dfs en la variable ruta_transversal

   