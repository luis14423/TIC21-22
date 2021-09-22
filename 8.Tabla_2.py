def tabla_2():
    print("***********************")
    print("*CALCULADORA DE TABLAS*")
    print("***********************")
    numero=input("De que numero quieres saber la tabla: ")
    for cont in range(0,11):
        print(str(numero)+" x "+str(cont)+" = "+str(numero*cont))
    print("FIN")
    
tabla_2()
