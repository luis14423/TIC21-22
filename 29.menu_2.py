def pinta_menu():
    print("**************************************")
    print("***               MENU             ***")
    print("**************************************")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. POTENCIACION")

def manda_error():
    print("ELECCION ERRONEA, NO SE PUEDE DIVIDIR POR 0")
    
def suma(no1,no2):
    respuesta=no1+no2
    return(respuesta)

def resta(no1,no2):
    respuesta=no1-no2
    return(respuesta)

def multiplicacion(no1,no2):
    respuesta=no1*no2
    return(respuesta)

def division(no1,no2):
    respuesta=no1/no2
    return(respuesta)

def potenciacion(no1,no2):
    respuesta=no1**no2
    return(respuesta)


def menu_2():
    #Pedimos dos numeros
    error=1
    while(error==1):
        no1=input("Introduce un numero: ")
        no2=input("Introduce otro numero: ")
        no1=float(no1)
        no2=float(no2)
        opcion=0
        
        pinta_menu()
        
        while(opcion<=0 or opcion>5):
            opcion=input(" ELIGE: ")
            if(no2==0.0 and opcion==4):
                error=1
                manda_error()
            else:
                error=0
                print("Has elegido la opcion "+str(opcion))
                
    #OPCION SUMA
    if(opcion==1):
        print(suma(no1,no2))
    #OPCION RESTA
    if(opcion==2):
        print(resta(no1,no2))
    #OPCION PRODUCTO
    if(opcion==3):
        print(multiplicacion(no1,no2))
    #OPCION COCIENTE
    if(opcion==4):
        print(division(no1,no2))
    #OPCION POTENCIACION
    if(opcion==5):
        print(potenciacion(no1,no2))
    
menu_2()
