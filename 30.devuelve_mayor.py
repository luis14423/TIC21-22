def devuelve_mayor(num1,num2,num3,num4):
    if(num1>num2 and num1>num3 and num1>num4):
        mayor=num1
    else:
        if(num2>num1 and num2>num3 and num2>num4):
            mayor=num2
        else:
            if(num4>num2 and num4>num1 and num4>num3):
                mayor=num4
            else:
                mayor=num3
    return(mayor)
def f():
    num1=input("No1: ")
    num2=input("No2: ")
    num3=input("No3: ")
    num4=input("No4: ")

    print(devuelve_mayor(num1,num2,num3,num4))
f()
