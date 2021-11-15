def devuelve_mayor(num1,num2,num3):
    if(num1>num2 and num1>num3):
        mayor=num1
    else:
        if(num2>num1 and num2>num3):
            mayor=num2
        else:
            mayor=num3
    return(mayor)

def f():
    num1=input("No1: ")
    num2=input("No2: ")
    num3=input("No3: ")

    print(devuelve_mayor(num1,num2,num3))
f()
