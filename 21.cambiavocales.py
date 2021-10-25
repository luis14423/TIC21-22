def cambiavocales():
    palabra=raw_input("dime una palabra ")
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=="a"):
           print("e")
        else:
            if(palabra[cont]=="e"):
                print("e")
            else:
                if(palabra[cont]=="i"):
                     print("e")
                else:
                    if(palabra[cont]=="o"):
                        print("e")
                    else:
                        print(palabra[cont])
                    if(palabra[cont]=="u"):
                        print("e")
        cont=cont+1
    print("TU PALABRA TRANSFORMADA ES: "+(palabra))
cambiavocales()
