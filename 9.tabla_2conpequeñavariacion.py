def tabla_3():
    numero=input("De que numero quieres saber la tabla: ")
    print("***********************")
    print("*TABLA DEL "+str(numero)+" *")
    print("***********************")
    
    for cont in range(0,11):
        print(" "+str(numero)+" x "+str(cont)+" = "+str(numero*cont))
    print("FIN")
    
tabla_3()
