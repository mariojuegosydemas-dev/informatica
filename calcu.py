def calcu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("")
    num=input("elige una opción ")
    print("")
    if num==1:
        print("introduce dos digitos para sumar")
        suma()
    if num==2:
        print("introduce dos digitos para restar")
        resta()
    if num==3:
        print("introduce dos digitos para restar")
        multi()
    if num==4:
        print("introduce dos digitos para restar")
        div()


        
def suma():
    a=input("primer numero ")
    b=input("segundo numero ")
    result=a+b
    print(str(a)+" + "+str(b)+" = "+str(result))

def resta():
    a=input("primer numero ")
    b=input("segundo numero ")
    result=a-b
    print(str(a)+" - "+str(b)+" = "+str(result))

def multi():
    a=input("primer numero ")
    b=input("segundo numero ")
    result=a*b
    print(str(a)+" * "+str(b)+" = "+str(result))

def div():
    a=float(input("primer numero "))
    b=float(input("segundo numero "))
    if b==0:
        print("0 no es un numero valido como denominador")
        div()
        return  
    result=a/b
    print(str(a)+" / "+str(b)+" = "+str(result))  
    
calcu()
