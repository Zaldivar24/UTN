def calcular_edad(anio_nacimiento):
    anio_actual = 2025   
    return anio_actual - anio_nacimiento

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = calcular_edad(anio_nacimiento)

print(f"Su edad es {edad} años.")
