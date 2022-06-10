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
                print("Todo esta realizado")
                print("El costo actual es: " +str(costo))
                print("Todos las locaciones de las ventanass estan limpias")
        
        '''
        En este control condicional se determina el estado de la ventana 1
        En caso de ser 0 se aplican las diferentes condiciones
        '''
        if estadoV1 == '0':
            """
            if para evaluar cada uno de los estados en la ventana 1

            """
            #La ventana ya se encuentra se encuentra limpia
            print("La ventana ya se encuentra limpia")
            print("El costo actual es: " +str(costo))
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
                #Pasamos a la segunda ventana
                objetivo["V2"]='0'
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
                    #Nos pasamos a la tercera ventana
                    objetivo["V3"]='0'
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
                         #Nos pasamos a la cuarta ventana
                        objetivo["V4"]='0'
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
                            #Nos pasamos a la ventana 5
                            objetivo["V5"]='0'
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
                                #Estado objetivo ventana 6
                                objetivo["V6"]='0'
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
                                    #Estado objetivo 7
                                    objetivo["V7"]='0'
                                    print("Valor del costo = "+str(costo))
                                    # Afirmamos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado ")
            else:
                #Decimos que todo ya esta realizado y no hay nada que hacer
                print("Todo esta realizado")
                #Valor actual del costo
                print("El costo actual es: " +str(costo))
                #Decimos que todas las ventanas ya estan limpias
                print("Todas las ventanas ya han sido limpiadas")
                
    #PROGRAMACION PARA LA SEGUNDA VENTANA
    elif locacion_ventana =='V2':
        """
        If para realizar toda la programacion de la ventana 2,
        como segunda locacion del agente robot limpiavidrios.
     
        """        
        print("El robot Limpiavidrios esta en la : "+locacion_ventana)
        # Ingresamos el estado de la locacion de la Ventana
        estadoV1 = input( "Ingrese el estado de la locacion V1")
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
        #If para evaluar los estados de la ventana dos
        if estadoV2 == '1':
             """
                Evaluamos el estado de la ventana 2 y pasamos de estado objetivo.
             """            
             print("La ventana 2 esta sucia")
             #esta sucia y cambiamos de estado
             objetivo["V2"]='0'
             #Limpiamos la ventana
             print("LIMPIANDO VENTANA   ....")
             #Afirmamos que esta limoia la ventana
             print("La ventana esta limpia ")
             #aumentamos el costo por cambio de estado
             costo+=1
             #imprimimos el valor del costo
             print("Valor del costo = "+str(costo))
            # Afirmamos que la ventana esta limpia
             print("La ventana 2 se ha limpiado ")
             
             #If para evaluar la ventana 1
             if estadoV1=='1':
                 
                 """
                  If para evaluar a la ventana 1
                 """
                 print("La ventana 1 esta sucia ") 
                 #Cambiamos de estado para limpiar la ventana
                 objetivo["V1"]='0'
                 #Simulamos la limpieza de la ventana
                 print("LIMPIANDO VENTANA   ....")
                 print("La ventana ya esta limpia")
                 #aumentamos el costo por cambio de estado
                 costo+=1
                #imprimimos el valor del costo
                 print("Valor del costo = "+str(costo))
                # Afirmamos que la ventana esta limpia
                 print("La ventana 1 se ha limpiado ")
                 #Evaluamos la ventana 3
                 if estadoV3=='1':
                     print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                     print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                     print("La ventana ya esta limpia ") #La ventana esta limpia
                     #cambio de costo
                     costo+=1
                     #Pasamos el estado objetivo
                     objetivo["V3"]='0'
                     #El costo aumenta
                     print("Valor del costo = "+str(costo))
                     #Decimos que la ventana esta limpia
                     print("La ventana 3 se ha limpiado")
                     #if para la ventana 4
                     if estadoV4=='1':
                         print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                         print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                         print("La ventana ya esta limpia ") #La ventana esta limpia
                         #cambio de costo
                         costo+=1
                         #Pasamos el estado objetivo
                         objetivo["V4"]='0'
                         #El costo aumenta
                         print("Valor del costo = "+str(costo))
                         #Decimos que la ventana esta limpia
                         print("La ventana 4 se ha limpiado")
                         #If para la ventana 5
                         if estadoV5=='1':
                             print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                             print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                             print("La ventana ya esta limpia ") #La ventana esta limpia
                             #cambio de costo
                             costo+=1
                             #Pasamos el estado objetivo
                             objetivo["V5"]='0'
                             #El costo aumenta
                             print("Valor del costo = "+str(costo))
                             #Decimos que la ventana esta limpia
                             print("La ventana 5 se ha limpiado")
                             
                             #If para la ventana 6
                             if estadoV6 =='1':
                                 print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                 print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                 print("La ventana ya esta limpia ") #La ventana esta limpia
                                  #cambio de costo
                                 costo+=1
                                 #Pasamos el estado objetivo
                                 objetivo["V6"]='0'
                                 #El costo aumenta
                                 print("Valor del costo = "+str(costo))
                                 #Decimos que la ventana esta limpia
                                 print("La ventana 6 se ha limpiado")
                                 
                                 
                                 #If para la ventana 7
                                 if estadoV7 =='1':
                                     print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                     print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                     print("La ventana ya esta limpia") #La ventana esta limpia
                                      #cambio de costo
                                     costo+=1
                                     #Pasamos el estado objetivo
                                     objetivo["V7"]='0'
                                     #El costo aumenta
                                     print("Valor del costo = "+str(costo))
                                     #Decimos que la ventana esta limpia
                                     print("La ventana 7 se ha limpiado")
        #If para evaluar cuando la ventana esta limpia
        if estadoV2=='0':
            #Las ventanas ya estan limpias
            print("La ventana 2 ya esta limpia")
            #El costo no cambia porque no hay cambio de estado
            costo=costo
            print("Valor del costo = "+str(costo))
            #if para la ventana 1
            if estadoV1 =='1':
                print("La ventana 1 esta sucia ") #Decimos que la ventana esta sucia
                #Cambiamos estado objetivo.
                objetivo["V1"]='0'
                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                print("La ventana ya esta limpia ") #La ventana esta limpia
                #cambio de costo
                costo+=1
                 #El costo aumenta
                print("Valor del costo = "+str(costo))
                #Decimos que la ventana esta limpia
                print("La ventana 1 se ha limpiado")
                #if para evaluar la ventana 3
                if estadoV3 =='1':
                    print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                    #Cambiamos estado objetivo.
                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                    print("La ventana ya esta limpia ") #La ventana esta limpia
                    #cambio de costo
                    costo+=1
                    objetivo["V3"]='0'
                   #El costo aumenta
                    print("Valor del costo = "+str(costo))
                    #Decimos que la ventana esta limpia
                    print("La ventana 3 se ha limpiado")
                    #if para evaluar la ventana 4
                    if estadoV4 =='1':
                        print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        objetivo["V4"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 4 se ha limpiado")
                        
                        #if para evaluar la ventana 5
                        if estadoV5 =='1':
                            print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            objetivo["V5"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 5 se ha limpiado")
                            
                            #If para evaluar la ventana 6
                            if estadoV6 =='1':
                                print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                objetivo["V6"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado")
                                
                                #If para evaluar la ventana 7
                                if estadoV7 =='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
            else:
                #Decimos que todo ya esta realizado y no hay nada que hacer
                print("Todo esta realizado")
                #Valor actual del costo
                print("El costo actual es: " +str(costo))
                #Decimos que todas las ventanas ya estan limpias
                print("Todas las ventanas ya han sido limpiadas")
    
    #Programacion locacion C
    elif locacion_ventana =='V3':
        """
        If para realizar toda la programacion de la ventana 3,
        como segunda locacion del agente robot limpiavidrios.
     
        """      
        print("El robot Limpiavidrios esta en la : "+locacion_ventana)
        # Ingresamos el estado de la locacion de la Ventana
        estadoV1 = input( "Ingrese el estado de la locacion V1")
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
        
        #if para evaluar la ventana 3
        if estadoV3=='1':
            print("La ventana 3 esta sucia")
            #esta sucia y cambiamos de estado
            objetivo["V3"]='0'
            #Limpiamos la ventana
            print("LIMPIANDO VENTANA   ....")
             #Afirmamos que esta limoia la ventana
            print("La ventana esta limpia ")
             #aumentamos el costo por cambio de estado
            costo+=1
             #imprimimos el valor del costo
            print("Valor del costo = "+str(costo))
            # Afirmamos que la ventana esta limpia
            print("La ventana 3 se ha limpiado ")
            
            #if para evaluar a la ventana 2
            if estadoV2 =='1':
                print("La ventana 2 esta sucia")
                #esta sucia y cambiamos de estado
                objetivo["V2"]='0'
                #Limpiamos la ventana
                print("LIMPIANDO VENTANA   ....")
                #Afirmamos que esta limoia la ventana
                print("La ventana esta limpia ")
                #aumentamos el costo por cambio de estado
                costo+=1
                #imprimimos el valor del costo
                print("Valor del costo = "+str(costo))
                # Afirmamos que la ventana esta limpia
                print("La ventana 2 se ha limpiado ")
                
                #if para evaluar la ventana 1
                if estadoV1 =='1':
                    print("La ventana 1 esta sucia")
                    #esta sucia y cambiamos de estado
                    objetivo["V1"]='0'
                    #Limpiamos la ventana
                    print("LIMPIANDO VENTANA   ....")
                    #Afirmamos que esta limoia la ventana
                    print("La ventana esta limpia ")
                    #aumentamos el costo por cambio de estado
                    costo+=1
                    #imprimimos el valor del costo
                    print("Valor del costo = "+str(costo))
                    # Afirmamos que la ventana esta limpia
                    print("La ventana 1 se ha limpiado ")
                    
                    #if para evaluar la ventana 4
                    if estadoV4 =='1':
                        print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        #Pasamos el estado objetivo
                        objetivo["V4"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 4 se ha limpiado")
                        
                        #if para evaluar la ventana 5
                        if estadoV5 =='1':
                            print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #Pasamos el estado objetivo
                            objetivo["V5"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 5 se ha limpiado")
                            
                            #if para evaluar la ventana 6
                            if estadoV6=='1':
                                print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #Pasamos el estado objetivo
                                objetivo["V6"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado")
                                
                                #if para evaluar la ventana 7 
                                if estadoV7 =='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #Pasamos el estado objetivo
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
        
        if estadoV3 =='0':
            #Las ventanas ya estan limpias
            print("La ventana 2 ya esta limpia")
            #El costo no cambia porque no hay cambio de estado
            costo=costo
            print("Valor del costo = "+str(costo))
            
            #if para la ventana 2
            if estadoV2=='1':
                print("La ventana 2 esta sucia ") #Decimos que la ventana esta sucia
                #Cambiamos estado objetivo.
                objetivo["V2"]='0'
                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                print("La ventana ya esta limpia ") #La ventana esta limpia
                #cambio de costo
                costo+=1
                 #El costo aumenta
                print("Valor del costo = "+str(costo))
                #Decimos que la ventana esta limpia
                print("La ventana 2 se ha limpiado")
                #if para evaluar la ventana 3
                if estadoV1=='1':
                    print("La ventana 1 esta sucia ") #Decimos que la ventana esta sucia
                    #Cambiamos estado objetivo.
                    objetivo["V1"]='0'
                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                    print("La ventana ya esta limpia ") #La ventana esta limpia
                    #cambio de costo
                    costo+=1
                    #El costo aumenta
                    print("Valor del costo = "+str(costo))
                    #Decimos que la ventana esta limpia
                    print("La ventana 1 se ha limpiado")
                    #if para evaluar la ventana 4
                    if estadoV4=='1':
                        print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        #Cambiamos el estado objetivo
                        objetivo["V4"]='0'
                    #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 4 se ha limpiado")
                        
                        #if para evaluar la ventana 5
                        if estadoV5 =='1':
                            print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #Cambiamos el estado objetivo
                            objetivo["V5"]='0'
                        #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 5 se ha limpiado")
                            
                            #if para evaluar la ventana 6
                            if estadoV6 =='1':
                                print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #Cambiamos el estado objetivo
                                objetivo["V6"]='0'
                            #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado")
                                
                                #if para evaluar la ventana 7
                                if estadoV7=='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #Cambiamos el estado objetivo
                                    objetivo["V7"]='0'
                                #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
            else:
                #Decimos que todo ya esta realizado y no hay nada que hacer
                print("Todo esta realizado")
                #Valor actual del costo
                print("El costo actual es: " +str(costo))
                #Decimos que todas las ventanas ya estan limpias
                print("Todas las ventanas ya han sido limpiadas")
                
    #PROGRAMACION PARA LA VENTANA V4
    elif locacion_ventana =='V4':
        """
        If para realizar toda la programacion de la ventana 4,
        como segunda locacion del agente robot limpiavidrios.
     
        """      
        print("El robot Limpiavidrios esta en la : "+locacion_ventana)
        # Ingresamos el estado de la locacion de la Ventana
        estadoV1 = input( "Ingrese el estado de la locacion V1")
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
        
        #if para evaluar la ventana 4
        if estadoV4 =='1':
            """
                Evaluamos el estado de la ventana 2 y pasamos de estado objetivo.
            """            
            print("La ventana 4 esta sucia")
            #Limpiamos la ventana
            print("LIMPIANDO VENTANA   ....")
            #Afirmamos que esta limoia la ventana
            print("La ventana esta limpia ")
            #aumentamos el costo por cambio de estado
            costo+=1
            #esta sucia y cambiamos de estado
            objetivo["V4"]='0'
            #imprimimos el valor del costo
            print("Valor del costo = "+str(costo))
            # Afirmamos que la ventana esta limpia
            print("La ventana 4 se ha limpiado ")
            
            #if para evaluar la ventana 1
            if estadoV1=='1':
                print("La ventana 1 esta sucia ") #Decimos que la ventana esta sucia
                #Cambiamos estado objetivo.
                objetivo["V1"]='0'
                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                print("La ventana ya esta limpia ") #La ventana esta limpia
                 #cambio de costo
                costo+=1
                #El costo aumenta
                print("Valor del costo = "+str(costo))
                #Decimos que la ventana esta limpia
                print("La ventana 1 se ha limpiado")
                
                #if para evaluar la ventana 2
                if estadoV2 =='1':
                    print("La ventana 2 esta sucia ") #Decimos que la ventana esta sucia
                    #Cambiamos estado objetivo.
                    objetivo["V2"]='0'
                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                    print("La ventana ya esta limpia ") #La ventana esta limpia
                    #cambio de costo
                    costo+=1
                    #El costo aumenta
                    print("Valor del costo = "+str(costo))
                    #Decimos que la ventana esta limpia
                    print("La ventana 2 se ha limpiado")
                    
                    #if para evaluar la ventnana 3
                    if estadoV3=='1':
                        print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        #Cambiamos estado objetivo.
                        objetivo["V3"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 3 se ha limpiado")
                        
                        #if para la ventana 5
                        if estadoV5=='1':
                            print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #Cambiamos estado objetivo.
                            objetivo["V5"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 5 se ha limpiado")
                            
                            #if para la ventana 6
                            if estadoV6 =='1':
                                print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #Cambiamos estado objetivo.
                                objetivo["V6"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado")
                                
                                #if para la ventana 7
                                if estadoV7 =='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #Cambiamos estado objetivo.
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
        if estadoV4 =='0':
            #Las ventanas ya estan limpias
            print("La ventana 4 ya esta limpia")
            #if para la ventana 1
            if estadoV1 =='1':
                print("La ventana 1 esta sucia ") #Decimos que la ventana esta sucia
                #Cambiamos estado objetivo.
                objetivo["V1"]='0'
                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                print("La ventana ya esta limpia ") #La ventana esta limpia
                #cambio de costo
                costo+=1
                 #El costo aumenta
                print("Valor del costo = "+str(costo))
                #Decimos que la ventana esta limpia
                print("La ventana 1 se ha limpiado")
                
                #if para evaluar la ventana 2
                if estadoV2 =='1':
                    
                    print("La ventana 2 esta sucia ") #Decimos que la ventana esta sucia
                    #Cambiamos estado objetivo.
                    objetivo["V2"]='0'
                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                    print("La ventana ya esta limpia ") #La ventana esta limpia
                    #cambio de costo
                    costo+=1
                    #El costo aumenta
                    print("Valor del costo = "+str(costo))
                    #Decimos que la ventana esta limpia
                    print("La ventana 2 se ha limpiado")
                    
                    #if para evaluar la ventana 3
                    if estadoV3 =='1':
                        print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        #estado objetivo
                        objetivo["V3"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 3 se ha limpiado")
                        
                        #if para evaluar la ventana 5
                        if estadoV5=='1':
                            print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #estado objetivo
                            objetivo["V5"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 5 se ha limpiado")
                            
                            #if para evaluar la ventana 6
                            if estadoV6 =='1':
                                print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #estado objetivo
                                objetivo["V6"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado")
                                
                                #if para evaluar la ventana 7
                                if estadoV7 =='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #estado objetivo
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
                                    
            else:
                #Decimos que todo ya esta realizado y no hay nada que hacer
                print("Todo esta realizado")
                #Valor actual del costo
                print("El costo actual es: " +str(costo))
                #Decimos que todas las ventanas ya estan limpias
                print("Todas las ventanas ya han sido limpiadas")
                
    # Programacion para la ventana 5
    elif locacion_ventana =='V5':
        
        """
        If para realizar toda la programacion de la ventana 5,
        como segunda locacion del agente robot limpiavidrios.
     
        """      
        print("El robot Limpiavidrios esta en la : "+locacion_ventana)
        # Ingresamos el estado de la locacion de la Ventana
        estadoV1 = input( "Ingrese el estado de la locacion V1")
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
        
        #if para evaluar la ventana 5
        if estadoV5=='1':
            
            print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
            #Cambiamos estado objetivo.
            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
            print("La ventana ya esta limpia ") #La ventana esta limpia
            #cambio de costo
            costo+=1
            #estado objetivo
            objetivo["V5"]='0'
            #El costo aumenta
            print("Valor del costo = "+str(costo))
             #Decimos que la ventana esta limpia
            print("La ventana 5 se ha limpiado")
            
            #if para evaluar  la ventana 1
            if estadoV1=='1':
                print("La ventana 1 esta sucia ") #Decimos que la ventana esta sucia
                #Cambiamos estado objetivo.
                objetivo["V1"]='0'
                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                print("La ventana ya esta limpia ") #La ventana esta limpia
                #cambio de costo
                costo+=1
                 #El costo aumenta
                print("Valor del costo = "+str(costo))
                #Decimos que la ventana esta limpia
                print("La ventana 1 se ha limpiado")
                
                #if para evaluar la ventana 2
                if estadoV2=='1':
                    print("La ventana 2 esta sucia ") #Decimos que la ventana esta sucia
                    #Cambiamos estado objetivo.
                    objetivo["V2"]='0'
                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                    print("La ventana ya esta limpia ") #La ventana esta limpia
                    #cambio de costo
                    costo+=1
                    #El costo aumenta
                    print("Valor del costo = "+str(costo))
                    #Decimos que la ventana esta limpia
                    print("La ventana 2 se ha limpiado")
                    
                    #if para evaluar la ventana 3
                    if estadoV3=='1':
                        print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        #estado objetivo
                        objetivo["V3"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 3 se ha limpiado")
                        
                        #if para evaluar la ventana 4
                        if estadoV4=='1':
                            
                            print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #estado objetivo
                            objetivo["V4"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 4 se ha limpiado")
                            
                            #if para evaluar la ventana 6
                            if estadoV6 =='1':
                                print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #estado objetivo
                                objetivo["V6"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado")
                                
                                #if para evaluar la ventana 7
                                if estadoV7 =='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #estado objetivo
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
                                    
        if estadoV5 =='0':
            #Las ventanas ya estan limpias
            print("La ventana 5 ya esta limpia")
            #El costo no cambia porque no hay cambio de estado
            costo=costo
            print("Valor del costo = "+str(costo)) 
            #evaluar ventana 1
            if estadoV1 =='1':
                
                print("La ventana 1 esta sucia ") 
                 #Cambiamos de estado para limpiar la ventana
                objetivo["V1"]='0'
                 #Simulamos la limpieza de la ventana
                print("LIMPIANDO VENTANA   ....")
                print("La ventana ya esta limpia")
                 #aumentamos el costo por cambio de estado
                costo+=1
                #imprimimos el valor del costo
                print("Valor del costo = "+str(costo))
                # Afirmamos que la ventana esta limpia
                print("La ventana 1 se ha limpiado ")
                
                #evaluar ventana 2
                if estadoV2=='1':
                    
                    print("La ventana 2 esta sucia ") 
                    #Cambiamos de estado para limpiar la ventana
                    objetivo["V2"]='0'
                    #Simulamos la limpieza de la ventana
                    print("LIMPIANDO VENTANA   ....")
                    print("La ventana ya esta limpia")
                    #aumentamos el costo por cambio de estado
                    costo+=1
                    #imprimimos el valor del costo
                    print("Valor del costo = "+str(costo))
                    # Afirmamos que la ventana esta limpia
                    print("La ventana 2 se ha limpiado ")
                    
                    #evaluar ventana 3
                    if estadoV3 =='1':
                        print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                         #cambio de costo
                        costo+=1
                        #estado objetivo
                        objetivo["V3"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 3 se ha limpiado")
                        
                        #evaluar ventana 4
                        if estadoV4 =='1':
                            print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #estado objetivo
                            objetivo["V4"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 4 se ha limpiado")
                            
                            #evaluar ventana 6
                            if estadoV6 =='1':
                                
                                print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #estado objetivo
                                objetivo["V6"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 6 se ha limpiado")
                                
                                #evaluar la ventana 7
                                if estadoV7 =='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #estado objetivo
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
                                    
            else:
                #Decimos que todo ya esta realizado y no hay nada que hacer
                print("Todo esta realizado")
                #Valor actual del costo
                print("El costo actual es: " +str(costo))
                #Decimos que todas las ventanas ya estan limpias
                print("Todas las ventanas ya han sido limpiadas")
                
    #Programacion para la ventana 6
    elif locacion_ventana =='V6':
        
        """
        If para realizar toda la programacion de la ventana 6,
        como segunda locacion del agente robot limpiavidrios.
     
        """      
        print("El robot Limpiavidrios esta en la : "+locacion_ventana)
        # Ingresamos el estado de la locacion de la Ventana
        estadoV1 = input( "Ingrese el estado de la locacion V1")
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
        
        #if para evaluar
        if estadoV6 =='1':
            print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
            #Cambiamos estado objetivo.
            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
            print("La ventana ya esta limpia ") #La ventana esta limpia
            #cambio de costo
            costo+=1
            #estado objetivo
            objetivo["V6"]='0'
             #El costo aumenta
            print("Valor del costo = "+str(costo))
            #Decimos que la ventana esta limpia
            print("La ventana 6 se ha limpiado")
            
            #evaluar ventana 1
            if estadoV1 =='1':
                print("La ventana 1 esta sucia ") #Decimos que la ventana esta sucia
                #estado objetivo
                objetivo["V1"]='0'
                #Cambiamos estado objetivo.
                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                print("La ventana ya esta limpia ") #La ventana esta limpia
                #cambio de costo
                costo+=1
                #El costo aumenta
                print("Valor del costo = "+str(costo))
                #Decimos que la ventana esta limpia
                print("La ventana 1 se ha limpiado")
                
                #evaluar ventana 2
                if estadoV2 =='1':
                    print("La ventana 2 esta sucia ") #Decimos que la ventana esta sucia
                    #estado objetivo
                    objetivo["V2"]='0'
                    #Cambiamos estado objetivo.
                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                    print("La ventana ya esta limpia ") #La ventana esta limpia
                    #cambio de costo
                    costo+=1
                    #El costo aumenta
                    print("Valor del costo = "+str(costo))
                    #Decimos que la ventana esta limpia
                    print("La ventana 2 se ha limpiado")
                    
                    #evaluar ventana 3
                    if estadoV3 =='1':
                        print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        #estado objetivo
                        objetivo["V3"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 3 se ha limpiado")
                        
                        #evaluar ventana 4
                        if estadoV4 =='1':
                            
                            print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #estado objetivo
                            objetivo["V4"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 4 se ha limpiado")
                            
                            #evaluar ventana 5
                            if estadoV5 =='1':

                                print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #estado objetivo
                                objetivo["V5"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 5 se ha limpiado")
                                
                                #evaluar ventana 7
                                if estadoV7 =='1':
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #estado objetivo
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
        if estadoV6=='0':
            #Las ventanas ya estan limpias
            print("La ventana 5 ya esta limpia")
            print("Todo esta realizado")
            #if para evaluar la ventana 1
            if estadoV1 =='1':
                print("La ventana 1 esta sucia ") 
                 #Cambiamos de estado para limpiar la ventana
                objetivo["V1"]='0'
                 #Simulamos la limpieza de la ventana
                print("LIMPIANDO VENTANA   ....")
                print("La ventana ya esta limpia")
                 #aumentamos el costo por cambio de estado
                costo+=1
                #imprimimos el valor del costo
                print("Valor del costo = "+str(costo))
                # Afirmamos que la ventana esta limpia
                print("La ventana 1 se ha limpiado ")
                
                #if para evaluar la ventana 2
                if estadoV2 =='1':
                    
                    print("La ventana 2 esta sucia ") 
                 #Cambiamos de estado para limpiar la ventana
                    objetivo["V2"]='0'
                    #Simulamos la limpieza de la ventana
                    print("LIMPIANDO VENTANA   ....")
                    print("La ventana ya esta limpia")
                    #aumentamos el costo por cambio de estado
                    costo+=1
                    #imprimimos el valor del costo
                    print("Valor del costo = "+str(costo))
                    # Afirmamos que la ventana esta limpia
                    print("La ventana 2 se ha limpiado ")
                    
                    #if para evaluar la ventana 3
                    if estadoV3 =='1':
                        print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                         #cambio de costo
                        costo+=1
                        #estado objetivo
                        objetivo["V3"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 3 se ha limpiado")
                        
                        #if para evaluar la ventana 4
                        if estadoV4 =='1':
                            print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #estado objetivo
                            objetivo["V4"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 4 se ha limpiado")
                            
                            #if para evaluar la ventana 5
                            if estadoV5 =='1':
                                print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #estado objetivo
                                objetivo["V5"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 5 se ha limpiado")
                                
                                #if para evaluar la ventana 7
                                if estadoV7 =='1':
                                    
                                    print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #estado objetivo
                                    objetivo["V7"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 7 se ha limpiado")
                                    
            else:
                #Decimos que todo ya esta realizado y no hay nada que hacer
                print("Todo esta realizado")
                #Valor actual del costo
                print("El costo actual es: " +str(costo))
                #Decimos que todas las ventanas ya estan limpias
                print("Todas las ventanas ya han sido limpiadas")
                

     #programacion para la ventana 7       
    elif locacion_ventana =='V7':
        
        """
        If para realizar toda la programacion de la ventana 7,
        como segunda locacion del agente robot limpiavidrios.
     
        """      
        print("El robot Limpiavidrios esta en la : "+locacion_ventana)
        # Ingresamos el estado de la locacion de la Ventana
        estadoV1 = input( "Ingrese el estado de la locacion V1")
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
        
        #if para evaluar la ventana 7
        if estadoV7 =='1':
            print("La ventana 7 esta sucia ") #Decimos que la ventana esta sucia
            #Cambiamos estado objetivo.
            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
            print("La ventana ya esta limpia ") #La ventana esta limpia
            #cambio de costo
            costo+=1
            #estado objetivo
            objetivo["V7"]='0'
            #El costo aumenta
            print("Valor del costo = "+str(costo))
            #Decimos que la ventana esta limpia
            print("La ventana 7 se ha limpiado")
            
            #If para evaluar la ventana 1
            if estadoV1 =='1':
                
                print("La ventana 1 esta sucia ") #Decimos que la ventana esta sucia
                #estado objetivo
                objetivo["V1"]='0'
                #Cambiamos estado objetivo.
                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                print("La ventana ya esta limpia ") #La ventana esta limpia
                #cambio de costo
                costo+=1
                #El costo aumenta
                print("Valor del costo = "+str(costo))
                #Decimos que la ventana esta limpia
                print("La ventana 1 se ha limpiado")
                
                #if para evaluar la ventana 2
                if estadoV2=='1':
                    
                    print("La ventana 2 esta sucia ") #Decimos que la ventana esta sucia
                    #estado objetivo
                    objetivo["V2"]='0'
                    #Cambiamos estado objetivo.
                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                    print("La ventana ya esta limpia ") #La ventana esta limpia
                    #cambio de costo
                    costo+=1
                    #El costo aumenta
                    print("Valor del costo = "+str(costo))
                    #Decimos que la ventana esta limpia
                    print("La ventana 2 se ha limpiado")
                    
                    #if para evaluar la ventana 3
                    if estadoV3=='1':
                        print("La ventana 3 esta sucia ") #Decimos que la ventana esta sucia
                        #Cambiamos estado objetivo.
                        print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                        print("La ventana ya esta limpia ") #La ventana esta limpia
                        #cambio de costo
                        costo+=1
                        #estado objetivo
                        objetivo["V3"]='0'
                        #El costo aumenta
                        print("Valor del costo = "+str(costo))
                        #Decimos que la ventana esta limpia
                        print("La ventana 3 se ha limpiado")
                        
                        #if para evaluar la ventana 4
                        if estadoV4 =='1':
                            print("La ventana 4 esta sucia ") #Decimos que la ventana esta sucia
                            #Cambiamos estado objetivo.
                            print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                            print("La ventana ya esta limpia ") #La ventana esta limpia
                            #cambio de costo
                            costo+=1
                            #estado objetivo
                            objetivo["V4"]='0'
                            #El costo aumenta
                            print("Valor del costo = "+str(costo))
                            #Decimos que la ventana esta limpia
                            print("La ventana 4 se ha limpiado")
                            #if para evaluar la ventana 5
                            if estadoV5 =='1':
                                print("La ventana 5 esta sucia ") #Decimos que la ventana esta sucia
                                #Cambiamos estado objetivo.
                                print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                print("La ventana ya esta limpia ") #La ventana esta limpia
                                #cambio de costo
                                costo+=1
                                #estado objetivo
                                objetivo["V5"]='0'
                                #El costo aumenta
                                print("Valor del costo = "+str(costo))
                                #Decimos que la ventana esta limpia
                                print("La ventana 5 se ha limpiado")
                                
                                #if para evaluar la ventana 6
                                if estadoV6 =='1':
                                    print("La ventana 6 esta sucia ") #Decimos que la ventana esta sucia
                                    #Cambiamos estado objetivo.
                                    print("LIMPIANDO VENTANA   ....") #Limpiamos la ventana
                                    print("La ventana ya esta limpia ") #La ventana esta limpia
                                    #cambio de costo
                                    costo+=1
                                    #estado objetivo
                                    objetivo["V6"]='0'
                                    #El costo aumenta
                                    print("Valor del costo = "+str(costo))
                                    #Decimos que la ventana esta limpia
                                    print("La ventana 6 se ha limpiado")
                                
                        
                    
                
                
            
            
        
                    
                                
                        
                    
                    
                
                
            
            
            
            
            
                                
                                
                            
                            
                            
                        
                        
                    
            
            
            
        
    
                                    
                                
                            
                            
                        
                    
                
                       
                                    
                                
                            
                            
                        
                    
                
            
        
                                            
                                    
                            
                         
                            
                    
                    
                
            
         
                                        
                                    
                                
                            
                        
                     
                     
                    
                
            
        
        
        
        
        
                                
                                
                            
                    
            
        
            
                                    
                        
                    
                    
            
            
                
                                    
                            
                        
                    
                
                
            
             
                                     
                            
                                     
                                 
                             
                             
                         
                     
                     
                     
                     
                     
                     
                     
                 
                                 
             
             
             
             
             
             
            
        
        
    
        



            



    


LimpiaVidrios()
