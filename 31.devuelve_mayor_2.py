def devuelve_mayor_10():
    mayor=input("Introduce un numero: ")
    for cont in range(1,11):
        num=input("Introduce otro numero: ")
        if(num>mayor):
            mayor=num
    print("EL MAYOR NUMERO ES: "+str(mayor))

devuelve_mayor_10()
    
