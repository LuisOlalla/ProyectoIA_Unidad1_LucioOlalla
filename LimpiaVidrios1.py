# PROYECTO UNIDAD 1 AGENTE ROBOT LIMPIAVIDRIOS EN UN EDIFICIO DE LA ESPE
# Integrantes: Carlos Lucio , Luis Olalla
# Curso: 6 to A
# Asignatura: Inteligencia Artificial
# Programar el agente
# Definimos funcíon del Robot Limpia Vidrios

import time
def LimpiaVidrios():
    """
    Funcion del robot que va a contener todo el control del flujo del programa
    mediante bloques de codigo de cada locación.
    
    contiene 2 diccionarios:
    
    Diccionario objetivo por el cual se va a correr el programa y evaluar cada estado. 
    objetivo = {'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0',
                'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '0', 'Ventana 7': '0'}
                
    Diccionario locaciones que imprime el estado actual del programa: 
    locaciones ={'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0',
                'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '0', 'Ventana 7': '0'}
    
    Costo para evaluar el cambio de estado del agente, inicializado en 0.             
    costo = 0
    """
    
    # Colocamos el estado objetivo del robot LimpiaVidrios.
    objetivo = {'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0',
                'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '0', 'Ventana 7': '0'}
    
    #Colocamos el estado actual de las locaciones del robot LimpiaVidrios
    locaciones = {'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0',
                'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '0', 'Ventana 7': '0'}
    
    costo = 0  # Esto es el esfuerzo que realiza el robot al cambiar de estado.
    
    #For que permite recorrer mediante una llave el diccionario del estado objetivo.
    for llave in locaciones.keys():
        # Imprime la locacion en la que se encuentra mediante la llave creada.
        print('Locación: ', llave)
        # Try que contiene todo el flujo del agente.
        try:
                #while que evalua las locaciones, cuando se tenga un valor adecuado.
                while True:
                    #Ingreso del estado en el que se encuentra la localidad
                    #Pregunta si la ventana esta sucia =1  y si esta limpia = 0
                    estado_localidad = input('¿La ventana esta sucia?\n0 = No \n1 = Si\n')
                    
                    #If para evaluar si el estado de la locacion es diferente de 0 y 1
                    if (estado_localidad !='0' and estado_localidad !='1'):
                        #Print en caso de que se ingresen valores diferentes de 0 y 1
                        print("Ingrese valores numéricos de 0 a 1")
                        
                        #Elif para evaluar la locacion cuando su estado es igual a 1
                    elif(estado_localidad == '1'):
                        # 1 significa sucio por lo tanto se limpia la ventana.
                        print('LIMPIANDO VENTANA...')
                        time.sleep(2)
                        #Print para detallar que la ventana se limpio correctamente.
                        print('La ventana se ha limpiado correctamente') 
                        #El costo aumenta debido al cambio de estado.
                        costo+=1
                        #Evalua las locaciones que contiene la llave para colocarlos al final del diccionario.
                        objetivo[llave] = estado_localidad   
                        #Imprime el costo actual en base a los estados que se realizan.
                        print('El  Costo actual es: ',str(costo)) 
                        #break para cerrar el bucle elif
                        break   
                          
                    #Elif para evaluar cuando la ventana esta limpia   
                    elif(estado_localidad =='0'):
                        #Print para avisar que la ventana esta limpia
                        print('LA VENTANA ESTA LIMPIA ')
                        #El costo se mantiene ya que no hay ningun cambio.
                        print(' El Costo actual es: ',str(costo))
                        #break para cerrar el bucle de ventana limpia
                        break
        #Control de excepcion como alias
        except Exception as e:
            #imprime la excepcion  que definimos anteriormente
            print(e)        
    #Print para immprimir las locaciones del agente en base al resultado final
    print(str(objetivo))
    
#Funcion limpiavidrios
LimpiaVidrios()