def mayor_y_posicion():
    numeros = [0] * 7  
    for i in range(7):
        numeros[i] = int(input(f"Ingrese el número  {i}: "))

    mayor = numeros[0]
    posicion = 0

    for i in range(1, len(numeros)):
        if numeros[i] > mayor:
            mayor = numeros[i]
            posicion = i

    print(f"El número mayor es {mayor} y se encuentra en la posición {posicion}.")

mayor_y_posicion()
