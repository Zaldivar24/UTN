numeros = [0] * 6

for i in range(len(numeros)):
    numeros[i] = float(input(f"Ingrese un número real {i}: "))

suma = 0
for i in range(len(numeros)):
    suma += numeros[i]

promedio = suma / len(numeros)

print("El promedio de los valores es:", promedio)
