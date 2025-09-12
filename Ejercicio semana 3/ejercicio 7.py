def invertir_array():
    numeros = [0] * 6
    for i in range(6):
        numeros[i] = int(input(f"Ingrese el número para la posición {i}: "))
    
    print("Array invertido:")
    for j in range(5, -1, -1):
        print(numeros[j])

invertir_array()
