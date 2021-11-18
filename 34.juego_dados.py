import random
def dados():
    x1=0
    y1=0
    z1=0

    x2=0
    y2=0
    z2=0

    puntos1=0
    puntos2=0
    
    
    print("""Introduzca el nombre de los jugadores""")
    no1=raw_input("JUGADOR 1: ")
    no2=raw_input("JUGADOR 2:")

    print("TURNO JUGADOR 1")
    conf1=raw_input("JUGADOR 1 escriba D: ")
    if (conf1=="D"):
        x1=random.randint(1,6)
        y1=random.randint(1,6)
        z1=random.randint(1,6)
        puntos1=x1+y1+z1

        print("Primer numero: "+str(x1))
        print("Segundo numero: "+str(y1))
        print("Tercer numero: "+str(z1))
        print("Resultado final: "+str(puntos1))

    print("TURNO JUGADOR 2")
    conf2=raw_input("JUGADOR 2 escriba D: ")
    if (conf2=="D"):
        x2=random.randint(1,6)
        y2=random.randint(1,6)
        z2=random.randint(1,6)
        puntos2=x2+y2+z2

        print("Primer numero: "+str(x2))
        print("Segundo numero: "+str(y2))
        print("Tercer numero: "+str(z2))
        print("Resultado final: "+str(puntos2))
    
    
    







dados()
