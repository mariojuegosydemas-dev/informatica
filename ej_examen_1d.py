#este programa sirve para sacar el promedio de 10 números y decirnos cual es el mayor número dentro de ese conjunto
def programa_1():
    max_num = input("Introduce un número: ")
    sum_nums = max_num
    i=0
    num2=max_num
    cadena2=True
    while(i<9):
        num = input("Introduce otro número ")
        sum_nums =sum_nums+ num
        if (num>num2):
            cadena=True
        else:
            cadena=False
            cadena2=False
        if num > max_num:
            max_num = num
        i=i+1
        num2=num
    print("The largest number is:"+str(max_num) )
    print("The average is:"+str(sum_nums/10))
    if(cadena2==True):
        print("es una cadena creciente")
    if(cadena2==False):
        print("no es una cadena creciente")

programa_1()   

