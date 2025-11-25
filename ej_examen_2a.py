def programa_1():
    letra_mayuscula=raw_input("Dime una letra ")
    curvi(letra_mayuscula)

def curvi(letra_mayuscula):
    minus="qwertyuiopasdfghjklñzxcvbnm"
    nocurva="AEFHIKLMNTVWXYZ"
    curva="BCDGJOPQRSUÑ"
    if letra_mayuscula in minus:
        print(0)
    if letra_mayuscula in nocurva:
        print(0)
    if letra_mayuscula in curva:
        print(1)
        
programa_1()
