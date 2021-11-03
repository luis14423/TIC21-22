def fecha_mes():
    fecha=raw_input("Introduce una fecha en formato dd/mm/aaaa: ")
    nombres_meses="EneroFebreroMarzoAbrilMayoJunioJulioAgostoSeptiembreOctubreNoviembreDiciembre"
    x=int(fecha[3])*10+int(fecha[4])
    mes_elegido=nombres_meses[3*x-3]+nombres_meses[3*x-2]+nombres_meses[3*x-1]
    print("El mes de esa fecha es "+mes_elegido+".")
fecha_mes()
