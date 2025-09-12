
numeros = [0] * 5


for i in range(len(numeros)):
    numeros[i] = int(input(f"Ingrese un número {i}: "))


print("Contenido del array:")
for i in range(len(numeros)):
    print(f"numeros[{i}] = {numeros[i]}")




