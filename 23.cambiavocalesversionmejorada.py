def a():
    palabra=raw_input("dime una palabra: ")
    cont=0
    vocal=raw_input("A que vocal quieres transformarlo: ")
    while(cont<len(palabra)):
        if(palabra[cont]in"aeiou"):
           print(vocal)
        else:
            print(palabra[cont])
        cont=cont+1





        
    print("TU PALABRA TRANSFORMADA ES: "+(palabra))
a()
