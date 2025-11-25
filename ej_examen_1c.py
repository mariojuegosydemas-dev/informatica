#este programa sirve para sacar el promedio de 10 números y decirnos cual es el mayor número dentro de ese conjunto
def programa_1():
    max_num = input("Introduce un número: ")
    sum_nums = max_num
    i=0
    while(i<9):
        num = input("Introduce otro número ")
        sum_nums =sum_nums+ num
        if num > max_num:
            max_num = num
        i=i+1
    print("The largest number is:"+str(max_num) )
    print("The average is:"+str(sum_nums/10))

programa_1()   

