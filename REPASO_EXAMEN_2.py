#Haz un programa que lea un numero
#y devuelva la suma de los numeros inferiores a el

def f():
    x=input("Introduce un numero: ")
    sum=0
    for cont in range(1,x):
        sum=sum+cont

    print("resultado: "+str(sum))
f()
