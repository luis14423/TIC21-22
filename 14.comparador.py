def A():
    
    x=input("Cuantos numeros vas a comparar: ")
    num=input("Dame un numero: ")
    mayor=num
    menor=num
    suma=0
    suma=suma+num
    
    for cont in range(1,x):
        num=input("Dame un numero: ")
        if(num>mayor):
            mayor=num
        if(num<menor):
            menor=num
        suma=suma+num
    media=float(suma)/float(x)
    
    print("El mayor numero es "+str(mayor))
    print("El menor numero es "+str(menor))
    print("La media es "+str(media))
A()
        
