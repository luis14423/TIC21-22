def menu():
    #Pedimos dos numeros
    error=1
    while(error==1):
        no1=input("Introduce un numero: ")
        no2=input("Introduce otro numero: ")
        no1=float(no1)
        no2=float(no2)
        opcion=0
        
        print("**************************************")
        print("***               MENU             ***")
        print("1. SUMAR")
        print("2. RESTAR")
        print("3. MULTIPLICAR")
        print("4. DIVIDIR")
        print("5. POTENCIACION")
        
        while(opcion<=0 or opcion>5):
            opcion=input(" ELIGE: ")
            if(no2==0 and opcion==4):
                error=1
                
        print("Has elegido la opcion "+str(opcion))
        #OPCION SUMA
        if(opcion==1):
            print(no1+no2)
        #OPCION RESTA
        if (opcion==2):
            print(no1-no2)
        #OPCION PRODUCTO
        if(opcion==3):
            print(no1*no2)
        #OPCION COCIENTE
        if(opcion==4):
            if(no2==0):
                print("ELECCION ERRONEA, NO SE PUEDE DIVIDIR POR 0")
                error=1
            else:
                error=0
                print(no1/no2)
        #OPCION POTENCIACION
        if(opcion==5):
            print(no1**no2)
    
menu()
