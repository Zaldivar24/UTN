numeros = [0] * 8

for i in range(len(numeros)):
    numeros[i] = int(input(f"Ingrese un número {i}: "))

contador = 0
for i in range(len(numeros)):
    if numeros[i] > 100:
        contador += 1

print("La cantidad de números mayores a 100 es:", contador)
