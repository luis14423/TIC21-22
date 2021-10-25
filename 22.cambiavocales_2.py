def cambiavocales_3():
    palabra=raw_input("dime una palabra ")
    cont=0
    palabra2=" "
    vocal=raw_input("dime una vocal ")
    while(cont<len(palabra)):
        if(palabra[cont]=="a"):
           print(vocal)
           palabra2=palabra2+vocal
        else:
            if(palabra[cont]=="e"):
                print(vocal)
                palabra2=palabra2+vocal
            else:
                if(palabra[cont]=="i"):
                     print(vocal)
                     palabra2=palabra2+vocal
                else:
                    if(palabra[cont]=="o"):
                        print(vocal)
                        palabra2=palabra2+vocal
                    else:
                        if(palabra[cont]=="u"):
                            print(vocal)
                            palabra2=palabra2+vocal
                        else:
                            palabra2=palabra2+palabra[cont]
                            print(palabra[cont])
        cont=cont+1
    print(palabra2)                  
               
cambiavocales_3()
