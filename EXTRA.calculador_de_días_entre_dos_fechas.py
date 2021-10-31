def A():
    mes="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    x=raw_input("Dime una fecha en formato dd/mm/aaaa ")
    y=raw_input("Dime otra fecha en formato dd/mm/aaaa ")

    mayor=0
    menor=0
    
    num_mesx=float(x[3]+x[4])*30.0 #Para simplificar el programa aproximamos que cada mes tiene 30 dias
    num_anox=float(x[6]+x[7]+x[8]+x[9])*365.0 #Para simplificar el programa aproximamos que cada año tiene 365 dias
    suma_x=float(x[0]+x[1])+num_mesx+num_anox
    
    num_mesy=float(y[3]+y[4])*30.0 #Para simplificar el programa aproximamos que cada mes tiene 30 dias
    num_anoy=float(y[6]+y[7]+y[8]+y[9])*365.0 #Para simplificar el programa aproximamos que cada año tiene 365 dias
    suma_y=float(y[0]+y[1])+num_mesy+num_anoy

    if(suma_x<suma_y):
        mayor=suma_y
        menor=suma_x
    else:
        mayor=suma_x
        menor=suma_y
    resta=mayor-menor
    print("Entre ambas fechas hay una diferencia de "+str(resta)+" días.")
A()
    
    
