#PROYECTO UNIDAD 1 AGENTE ROBOT LIMPIAVIDRIOS EN UN EDIFICIO DE LA ESPE
#Integrantes: Carlos Lucio , Luis Olalla
#Curso: 6 to A
#Asignatura: Inteligencia Artificial

#Programar el agente

#Definimos funcíon del Robot Limpia Vidrios
def LimpiaVidrios():
    """
    Funcion del robot que va a contener todo el control del flujo del programa
    mediante bloques de codigo de cada locación.
    """  
    #Colocamos el estado objetivo de nuestro agente.
    objetivo = {'V1':'0','V2':'0','V3':'0','V4':'0','V5':'0','V6':'0','V7':'0'}
    esfuerzo = 0 #Esto es el esfuerzo que realiza el robot al cambiar de estado.
    
    #Estados del robot LimpiaVidrios
    print("ESTADOS DEL ROBOT LIMPIA VIDRIOS: ")
    print("Ventana Sucia = 1") #Si esta en 1 significa que hay ventanas sin limpiar.
    print("Ventana Limpia = 0 ") #Si esta en 0 es porque no hjay ventanas sucias.
    
    #Las locaciones o escenarios de nuestro robot son:
    print("LOCACIONES DEL ROBOT LIMPIA VIDRIOS:  ")
    print("Ventana 1 = V1\nVentana 2 = V2\nVentana 3 = V3\nVentana 4 = V4") #Todas las locaciones del robot, en este caso son las locaciones del edificion como ventanas.
    print("Ventana 5 = V5\nVentana 6 = V6\nVentana 7 = V7")#Todas las locaciones del robot, en este caso son las locaciones del edificion como ventanas.
    
      
    
    
    

LimpiaVidrios()