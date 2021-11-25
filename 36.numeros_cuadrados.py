def f():
    linea=" "
    fil=" "
    num=input("dame un numero: ")
    for fil in range(1,num+1):
        if(fil%2==1):
            letra="1"
        else:
            letra="0"
        for col in range(1,num+1):
            linea=linea+letra
        print(linea)
        linea=" "

f()
