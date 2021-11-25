def F():
    
    #INTRODUCCION
    print("*********************************")
    print("********CALCULADORA DE NOTA******")
    print("*********************************")
    print("")
    print("Por favor introduzca las carreras que le gustaria cursar en orden de preferencia")
    print("")
    carrera1=raw_input("Carrera numero 1: ")
    carrera2=raw_input("Carrera numero 2: ")
    carrera3=raw_input("Carrera numero 3: ")

    #FASE OBLIGATORIA EVAU
    print("Comenzaremos con las notas de los examenes de la fase obligatoria, siga las instrucciones introduciendo las notas del 0 al 10")
    print("")
    mates=input("Introduzca su media en el examen de matematicas: ")
    lengua=input("Introduzca su media en el examen de lengua: ")
    historia=input("Introduzca su media en el examen de historia: ")
    ingles=input("Introduzca su media en el examen de ingles: ")
        
    mates=float(mates)
    lengua=float(lengua)
    historia=float(historia)
    ingles=float(ingles)

    media_aritmetica=(mates+lengua+ingles+historia)/4.0
    
    if(media_aritmetica<4.0):
        print("Dado que la puntuacion de la fase obligatoria no es mayor que 4, no mediara")
        media_aritmetica=0
    else:
        print("la nota de la fase obligatoria de la EVAU es de "+str(media_aritmetica))
        
    print("")
    evau=media_aritmetica*0.4

    #NOTA MEDIA DE BACHILLERATO(NMB)
    nmb=input("Introduzca su nota media de Bachillerato: ")
    nmb=float(nmb)
    nmb=0.6*nmb

    #NOTA DE ACCESO
    acceso=evau+nmb
    print(acceso)
    finalizar=0
    if(acceso<5):
        print("Dado que no se supera el 5, queda suspendida la nota de acceso")
        finalizar=1
    else:
        print("Tu nota de acceso es de "+str(acceso))
    
    
    #FASE VOLUNTARIA
    if(finalizar==0):
        voluntaria1=input("Introduzca la puntuacion de la primera asignatura voluntaria: ")
        voluntaria1=float(voluntaria1)
        if(voluntaria1<5):
            print("Dado que este examen voluntario no fue aprobado no sera tenido en cuenta para la media")
            voluntaria1=0
        
        voluntaria2=input("Introduzca la puntuacion de la segunda asignatura voluntaria: ")
        voluntaria2=float(voluntaria2)
        if(voluntaria2<5):
            print("Dado que este examen voluntario no fue aprobado no sera tenido en cuenta para la media")
            voluntaria2=0
        
        evau_voluntaria=(voluntaria1*0.2)+(voluntaria2*0.2)
    
    #NOTA DE ADMISION
        admision=acceso+evau_voluntaria
        print("Tu nota de admision es "+str(admision))
            
F()
