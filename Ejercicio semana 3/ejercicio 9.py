def reemplazar_pares():
    numeros = [0] * 10
    for i in range(10):
        numeros[i] = int(input(f"Ingrese el número para la posición {i}: "))

    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            numeros[i] = 0

    print("Array resultante:")
    for i in range(len(numeros)):
        print(f"Posición {i}: {numeros[i]}")

reemplazar_pares()
