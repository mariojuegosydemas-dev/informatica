def suma_digitos_2():
    #Pedir un número y lo leo como una cadena
    numero=input("Dime un número de varias cifras: ")
    suma=0
    permanecer=True
    while(permanecer==True):
        suma=suma+(numero%10)
        numero=numero/10
        print("suma= "+str(suma)+" numero= "+str(numero))
        if(numero<10):
            suma=suma+numero
            permanecer=False
    print(suma)

suma_digitos_2()
