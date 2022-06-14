# PROYECTO UNIDAD 1 AGENTE ROBOT LIMPIAVIDRIOS EN UN EDIFICIO DE LA ESPE
# Integrantes: Carlos Lucio , Luis Olalla
# Curso: 6 to A
# Asignatura: Inteligencia Artificial

# Programar el agente

# Definimos funcíon del Robot Limpia Vidrios


from cmath import e


def LimpiaVidrios():
    """
    Funcion del robot que va a contener todo el control del flujo del programa
    mediante bloques de codigo de cada locación.
    """
    # Colocamos el estado objetivo de nuestro agente.
    objetivo = {'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0',
                'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '0', 'Ventana 7': '0'}
    locaciones = {'Ventana 1': '0', 'Ventana 2': '0', 'Ventana 3': '0',
                'Ventana 4': '0', 'Ventana 5': '0', 'Ventana 6': '0', 'Ventana 7': '0'}
    costo = 0  # Esto es el esfuerzo que realiza el robot al cambiar de estado.


    

    for llave in objetivo.keys():
        
        
        print('Locación: ', llave)

        try:
                while True:
                    
                    estado_localidad = str(input('¿La ventana esta sucia?\n0 = No \n1 = Si\n'))
                    if (estado_localidad !='0' and estado_localidad !='1'):
                        print("Ingrese valores numéricos de 0 a 1")
                        
                    
                    elif(estado_localidad == '1'):
                        print('Limpiando la ventana...')
                        print('La ventana se ha limpiado correctamente') 
                        costo+=1
                        locaciones[llave] = estado_localidad   
                        print('El  Costo actual es: ',str(costo)) 
                        break            
                    elif(estado_localidad =='0'):

                        print('La ventana esta limpia ')
                        print(' El Costo actual es: ',str(costo))
                        break
        except Exception as e:


            print(e)
            
    print(str(locaciones))
    print(str(objetivo))

LimpiaVidrios()