def suma_digitos():
    #Pedir un número y lo leo como una cadena
    numero=raw_input("Dime un número de varias cifras: ")
    longitud=len(numero)
    suma=0
    for cont in range(0,longitud):
        suma=suma+int(numero[cont])
    #trocearlo en cifras
    print(suma)
    #Sumo o acumulo las cifras en una variable acumuladora
suma_digitos()
