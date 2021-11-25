def f():
    nombre=raw_input("Dime tu nombre: ")
    if(nombre[0]=="A" or nombre[0]=="Z"):
        print("Tu nombre va el primero o el ultimo")
    else:
        print("Tu nombre no va el primero")
    for cont in range(1,4):
        print("ADIOS")

f()
