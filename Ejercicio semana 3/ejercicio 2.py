numeros = [0] * 10

for i in range (len(numeros)):
    numeros[i] = int(input(f"ingrese un numero {i}: "))

suma = 0
for i in range(len(numeros)):
    suma += numeros[i]

print("La suma de todos los numeros es:", suma)