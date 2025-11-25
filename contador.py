def contador():
    palabra = raw_input("dime una palabra ")  
    nump = len(palabra)
    vocal = ("a", "e", "i", "o", "u")  
    numv = 0
    numo = 0
    print("tiene " + str(nump) + " letras")
    for cont in range(0, nump):
        if palabra[cont] in vocal:  
            numv = numv + 1
    numc= nump-numv
    print("tiene "+str(numv)+" vocales")
    print("tiene "+str(numc)+" consonantes")
    for cont in range(0, nump):
        if palabra[cont] == "o":  
            numo = numo + 1
    print("tiene " + str(numo) + " veces la letra o")
 
contador()
