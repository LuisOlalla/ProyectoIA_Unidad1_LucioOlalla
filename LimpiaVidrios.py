# PROYECTO UNIDAD 1 AGENTE ROBOT LIMPIAVIDRIOS EN UN EDIFICIO DE LA ESPE
# Integrantes: Carlos Lucio , Luis Olalla
# Curso: 6 to A
# Asignatura: Inteligencia Artificial

# Programar el agente

# Definimos funcíon del Robot Limpia Vidrios
def LimpiaVidrios():
    """
    Funcion del robot que va a contener todo el control del flujo del programa
    mediante bloques de codigo de cada locación.
    """
    # Colocamos el estado objetivo de nuestro agente.
    objetivo = {'V1': '0', 'V2': '0', 'V3': '0',
                'V4': '0', 'V5': '0', 'V6': '0', 'V7': '0'}
    costo = 0  # Esto es el esfuerzo que realiza el robot al cambiar de estado.

    # Estados del robot LimpiaVidrios
    print("ESTADOS DEL ROBOT LIMPIA VIDRIOS: ")
    # Si esta en 1 significa que hay ventanas sin limpiar.
    print("Ventana Sucia = 1")
    # Si esta en 0 es porque no hjay ventanas sucias.
    print("Ventana Limpia = 0 ")

    # Las locaciones o escenarios de nuestro robot son:
    print("LOCACIONES DEL ROBOT LIMPIA VIDRIOS:  ")
    # Todas las locaciones del robot, en este caso son las locaciones del edificion como ventanas.
    print("Ventana 1 = V1\nVentana 2 = V2\nVentana 3 = V3\nVentana 4 = V4")
    # Todas las locaciones del robot, en este caso son las locaciones del edificion como ventanas.
    print("Ventana 5 = V5\nVentana 6 = V6\nVentana 7 = V7")

    # Ingreso de locaciones del robot LimpiaVidrios
    locacion_ventana = input("Ingrese el escenario o locacion de la ventana :")
    # Realizamos los if de cada locación, vamos a empezar con la Ventana 1 = V1
    # Si la locacion es V1, entonces el robot LimpiaVidrios esta en la Ventana 1
    if locacion_ventana == 'V1':
        """
        If locacion_ventana nos permite ingresar el estado para la locacion de la ventana 1,
        y despues para las demas ventanas.

        """
        # Mandamos un print que nos dice que el robot LimpiaVidrios esta en la locacion V1
        print("El robot Limpiavidrios esta en la Ventana 1 : ")
        # Ingresamos el estado de la locacion de la Ventana
        estadoV1 = input(
            "Ingrese el estado de la locacion : " + locacion_ventana)
        # Ingreso del estado para la locacion de la ventana 2
        estadoV2 = input("Ingrese el estado de la locacion V2 : ")
        # Ingreso del estado para la locacion de la ventana 3
        estadoV3 = input("Ingrese el estado de la locacion V3 : ")
       # Ingreso del estado para la locacion de la ventana 4
        estadoV4 = input("Ingrese el estado de la locacion V4 : ")
       # Ingreso del estado para la locacion de la ventana 5
        estadoV5 = input("Ingrese el estado de la locacion V5 : ")
        # Ingreso del estado para la locacion de la ventana 6
        estadoV6 = input("Ingrese el estado de la locacion V6 : ")
       # Ingreso del estado para la locacion de la ventana 7
        estadoV7 = input("Ingrese el estado de la locacion V7 : ")
        # En caso de que sea 0 la ventana esta limpia
        if estadoV1 == '1':
            """
            if para evaluar cada uno de los estados en la ventana 1

            """
            # Dado que la ventana 1 es igual a  1 esta sucia
            print("En la locación: "+locacion_ventana +
                  ", la ventana esta sucia ")
            # Asignamos el estado objetivo a 0 para que pase la ventana a estar limpia.
            objetivo["V1"] = '0'
            # Simulación de que el robot esta limpiando la ventana 1
            print("LIMPIANDO VENTANA 1 ....")
            # Verificacion de que la ventana esta limpia
            print("En la locacion : "+locacion_ventana +
                  ", el robot ha limpiado la ventana ")
            # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
            costo += 1
            # Verificamos el valor del costo.
            print("Valor del costo = "+str(costo))
            # Realizamos el if para la ventana 2
            if estadoV2 == '1':
                """
                If para evaluar los estados de la ventana 2, en este caso la ventana esta sucia por lo cual se debe cambiar de estado.
                """
                # En caso de que sea  1 la ventana esta sucia
                print("En la locación: "+estadoV2 + ", la ventana esta sucia ")
                # Simulación de que el robot esta limpiando la ventana
                print("LIMPIANDO VENTANA 2  ....")
                # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                costo += 1
                print("Valor del costo = "+str(costo))
                # Afirmamos que la ventana esta limpia
                print("La ventana 2 se ha limpiado ")

                # Realizamos el if para la ventana 3
                if estadoV3 == '1':
                    """
                    If para evaluar los estados de la ventana 3, en este caso la ventana esta sucia por lo cual se debe cambiar de estado.
                    """
                    # En caso de que sea  1 la ventana esta sucia
                    print("En la locación: "+estadoV3 +
                          ", la ventana esta sucia ")
                    # Simulación de que el robot esta limpiando la ventana
                    print("LIMPIANDO VENTANA 3  ....")
                    # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                    costo += 1
                    print("Valor del costo = "+str(costo))
                    # Afirmamos que la ventana esta limpia
                    print("La ventana 3 se ha limpiado ")
                    if estadoV4 == '1':
                        # En caso de que sea  1 la ventana esta sucia
                        print("En la locación: "+estadoV4 +
                              ", la ventana esta sucia ")
                        # Simulación de que el robot esta limpiando la ventana
                        print("LIMPIANDO VENTANA 4  ....")
                        # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                        costo += 1
                        print("Valor del costo = "+str(costo))
                        # Afirmamos que la ventana esta limpia
                        print("La ventana 4 se ha limpiado ")
                        if estadoV5 == '1':
                            # En caso de que sea  1 la ventana esta sucia
                            print("En la locación: "+estadoV5 +
                                  ", la ventana esta sucia ")
                            # Simulación de que el robot esta limpiando la ventana
                            print("LIMPIANDO VENTANA 5  ....")
                            # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                            costo += 1
                            print("Valor del costo = "+str(costo))
                            # Afirmamos que la ventana esta limpia
                            print("La ventana 5 se ha limpiado ")
                            if estadoV6 == '1':
                                # En caso de que sea  1 la ventana esta sucia
                                print("En la locación: "+estadoV6 +
                                      ", la ventana esta sucia ")
                                # Simulación de que el robot esta limpiando la ventana
                                print("LIMPIANDO VENTANA 6  ....")
                                # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                                costo += 1
                                print("Valor del costo = "+str(costo))
                                # Afirmamos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado ")
                                if estadoV7 == '1':
                                    # En caso de que sea  1 la ventana esta sucia
                                    print("En la locación: "+estadoV7 +
                                          ", la ventana esta sucia ")
                                    # Simulación de que el robot esta limpiando la ventana
                                    print("LIMPIANDO VENTANA 7  ....")
                                    # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                                    costo += 1
                                    print("Valor del costo = "+str(costo))
                                    # Afirmamos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado ")
                '''
                Segundo caso en donde se no realiza cambios en ninguna locación
                El agente no realizará ninguna acción
                Parámetros:
                    estadoV2:str
                        Determina el estado en el que se encuentra el agente
                Retorna:
                    costo = costo
                '''
            else:
                print("Ninguna acción a realizar")
                print("El costo actual es: " +str(costo))
    else:
        print("Todas las ventanas estan limpias")
        print("Valor del costo actual =" + str(costo))
        print("Todos las locaciones de las ventanadas estan limpias")

        if estadoV1 == '0':
            print("La ventana 1 ya se encuentra limpia")
            if estadoV2 == '1':
                """
                If para evaluar los estados de la ventana 2, en este caso la ventana esta sucia por lo cual se debe cambiar de estado.
                """
                # En caso de que sea  1 la ventana esta sucia
                print("En la locación: "+estadoV2 + ", la ventana esta sucia ")
                # Simulación de que el robot esta limpiando la ventana
                print("LIMPIANDO VENTANA 2  ....")
                # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                costo += 1
                print("Valor del costo = "+str(costo))
                # Afirmamos que la ventana esta limpia
                print("La ventana 2 se ha limpiado ")
                if estadoV3 == '1':
                    """
                    If para evaluar los estados de la ventana 3, en este caso la ventana esta sucia por lo cual se debe cambiar de estado.
                    """
                    # En caso de que sea  1 la ventana esta sucia
                    print("En la locación: "+estadoV3 +
                          ", la ventana esta sucia ")
                    # Simulación de que el robot esta limpiando la ventana
                    print("LIMPIANDO VENTANA 3  ....")
                    # El costo aumenta ya que realizo un esfuerzo al cambiar de estado.
                    costo += 1
                    print("Valor del costo = "+str(costo))
                    # Afirmamos que la ventana esta limpia
                    print("La ventana 3 se ha limpiado ")

            



    


LimpiaVidrios()
