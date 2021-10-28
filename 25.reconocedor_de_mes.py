def A():
    mes="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    cont=0
    x=raw_input("Introduce una fecha en el formato dd/mm/aa: ")
    z=x[3]+x[4]
    s=int(z)*3
    palabra=mes[s-3]+mes[s-2]+mes[s-1]
    print(palabra)
    
    
A()
