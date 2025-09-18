def contrasena ():
    nombre=raw_input("dime tu nombre ")
    apellido1=raw_input("dime tu 1º apellido ")
    apellido2=raw_input("dime tu 2º apellido ")
    ano=raw_input("dime tu año de nacimiento ")
    print("tu contrseña es "+nombre[:3]+apellido1[:3]+apellido2[:3]+ano[2:])

contrasena()
