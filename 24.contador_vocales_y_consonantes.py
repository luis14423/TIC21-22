def A():
    palabra=raw_input("Dime una palabra: ")
    cont=0
    voc=0
    cons=0
    while(cont<len(palabra)):
        if(palabra[cont] in "aeiou"):
            voc=voc+1
        else:
            cons=cons+1
        cont=cont+1

    
    print("Vocales: "+str(voc))
    print("Consonantes: "+str(cons))
    print("Letras: "+str(voc+cons))
A()
