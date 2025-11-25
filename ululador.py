def ululador():
    frase_entrada=raw_input("dime algo coherente ")
    frase_salida=""
    vocales_m="aeiou"
    vocales_M="AEIOU"
    for cont in range(0,len(frase_entrada)):
        if(frase_entrada[cont]in vocales):
            frase_salida=frase_salida+'u'
        else:
            frase_salida=frase_salida+frase_entrada[cont]
    print(frase_salida)
        
ululador()
