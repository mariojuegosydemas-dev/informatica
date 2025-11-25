def contador():
    palabra = raw_input("dime una palabra ")  
    nump = len(palabra)
    vocal = ("aeiouAEIOU")
    consonant = ("qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM")
    letras=("qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM")
    numv = 0
    numo = 0
    numc = 0
    numl = 0
    nume = 0
    for cont in range(0, nump):
        if palabra[cont] in vocal:  
            numv = numv + 1
    for cont in range(0, nump):
        if palabra[cont] in consonant:  
            numc = numc + 1
    for cont in range(0, nump):
        if palabra[cont] in letras:  
            numl = numl + 1
    for cont in range(0, nump):
        if palabra[cont] == "o":  
            numo = numo + 1
    for cont in range(0,nump):
        if palabra[cont]== " ":
            nume = nume +1
    print("tiene " + str(numl) + " letras")
    print("tiene "+str(numv)+" vocales")
    print("tiene "+str(numc)+" consonantes")
    print("tiene "+str(nume + 1)+" palabras")
    if numo == 1:
        print("tiene " + str(numo) + " vez la letra o")
    else:
       print("tiene " + str(numo) + " veces la letra o") 
    cifrado=""
    for letra in palabra:
        if letra == "z":
            cifrado += "a"
        else:
            if letra == " ":
                cifrado += " "
            else:
                cifrado += chr(ord(letra) + 1)
            
    print(cifrado)

contador()


    

