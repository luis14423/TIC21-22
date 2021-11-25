def f():
    x=input("Hasta donde cuento?: ")
    suma=0
    sumimpares=0
    sumpares=0
    pares=0
    impares=0
    for cont in range(1,x+1):
        print(cont)
        suma=suma+cont
        if(cont%2==0):
            sumpares=sumpares+cont
            pares=pares+1
        else:
            sumimpares=sumimpares+cont
            impares=impares+1

    print("El sumatorio desde 1 hasta "+str(x)+" es igual a "+str(suma))
    print("El sumatorio de numeros pares desde 1 hasta "+str(x)+" es igual a "+str(sumpares))
    print("El sumatorio de numeros pares desde 1 hasta "+str(x)+" es igual a "+str(sumimpares))
    print("Hay "+str(pares)+" numeros pares")
    print("Hay "+str(impares)+" numeros impares")

def comparador():
    x=input("Dime un numero: ")
    z=input("Cuantos numeros quieres comparar?: ")
    mayor=x
    menor=x
    for cont in range(1,z+1):
        x=input("Dime un numero: ")
        if(x>mayor):
            mayor=x
        if(x<menor):
            menor=x

    print(mayor)
    print(menor)

def palabras():
    x=raw_input("Dime tu nombre: ")
    print("Tu nombre empieza por la letra "+x[0])
    print("Voy a deletrear tu nombre ")
    for cont in range(0,len(x)):
        print(x[cont])

def vocales():
    x=raw_input("Introduce una palabra: ")
    for cont in range(0,len(x)):
        if(x[cont] in "AEIOUaeiou"):
            print("e")
        else:
            print(x[cont])
    print(x)

def bucle():
    x=input("Desde donde quieres hacer la cuenta atras?: ")
    #for cont in range(x,0,-1):
        #print(cont)
    while(x>0):
        print(x)
        x=x-1

def juego():
    import random
    suma=0
    for cont in range(1,4):
        x=random.randint(1,6)
        suma=suma+x
        print(x)

def mes():
    lista=" EneFebMarAbrMayJunJulAgoSepOctNovDic"
    x=raw_input("Introduce una fecha en formato dd/mm/aaaa: ")
    mes=10*int(x[3])+int(x[4])
    resultado=lista[3*mes-2]+lista[3*mes-1]+lista[3*mes]
    print(resultado)

def sumar(a,b):
    return(a+b)
def z():
    a=input("Dime un numero: ")
    b=input("Dime otro numero: ")
    print(sumar(a,b))


              
        
