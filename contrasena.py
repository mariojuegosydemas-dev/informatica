def contrasena ():
    nombre=raw_input("dime tu nombre ")
    apellido1=raw_input("dime tu 1� apellido ")
    apellido2=raw_input("dime tu 2� apellido ")
    ano=raw_input("dime tu a�o de nacimiento ")
    print("tu contrse�a es "+nombre[:3]+apellido1[:3]+apellido2[:3]+ano[2:])

contrasena()
