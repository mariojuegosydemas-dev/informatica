#Introduces una frase y el programa te cuenta
#1. Número de letras
#2. Número de consonantes
#3. Número de vocales
#4. Número de palabras
#5. Número de veces que aparece la letra o
#6. Encripta el mensaje sustituyendo cada letra por la siguiente en el
#abecedario

def menu():
    # MENU
    print("Elige una opcion (1-6): ")
    print("1. Contar el numero de letras")
    print("2. Contar el numero de consonantes")
    print("3. Contar el numero de vocales")
    print("4. Contar el numero de palabras")
    print("5. Contar el numero de de veces que aparece la letra o")
    print("6. Encriptar el mensaje")

def contar_letras(texto): #1
    print("Tiene "+str(len(texto))+" caracteres")

def contar_consonantes(texto): #2
    n_consonantes=0
    vocales="aeiouAEIOU"
    numero="1234567890"
    for letra in texto:
        if(not((letra in vocales) or (letra==" ") or(letra in numero))):
            n_consonantes=n_consonantes+1
    print("Tiene "+str(n_consonantes)+ " consonantes")

def contar_vocales(texto): #3
    n_vocales=0
    vocales="aeiouAEIOU"
    for letra in texto:
        if letra in vocales:
            n_vocales=n_vocales+1
    print("Tiene "+str(n_vocales)+" vocales")

def contar_palabras(texto): #4
    n_palabras=0
    for letra in texto:
        if letra==" ":
            n_palabras=n_palabras+1
    print("Tiene "+str(n_palabras+1)+" palabras")

def contar_oes(texto): #5
    n_o=0
    for letra in texto:
        if letra=="o":
            n_o=n_o+1
    print("tiene "+str(n_o)+" vez la letra o")

def encriptar(texto):
    cifrado=""
    for letra in texto:
        if letra == "z":
            cifrado += "a"
        else:
            if letra == " ":
                cifrado += " "
            else:
                cifrado += chr(ord(letra) + 1)
            
    print(cifrado)

def contador_total():
    #Pido el texto
    texto=raw_input("Introduce una frase: ")
    menu()
    opcion=input("ELIGE UNA OPCION (1-6): ")
    if(opcion==1):
        contar_letras(texto)
    if(opcion==2):
        contar_consonantes(texto)
    if(opcion==3):
        contar_vocales(texto)
    if(opcion==4):
        contar_palabras(texto)
    if(opcion==5):
        contar_oes(texto)
    if(opcion==6):
        encriptar(texto)
   
contador_total()
