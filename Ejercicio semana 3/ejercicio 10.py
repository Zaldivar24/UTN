def primera_aparicion(array, numero):
    for i in range(len(array)):
        if array [i] == numero:
            return i
    return -1

numeros = [3, 5, 7, 2, 9, 1]
buscar = int(input("ingrese el numero a buscar: "))

posicion = primera_aparicion(numeros, buscar)

if posicion != -1:
    print(f"el numero {buscar} aparece primero en la posicion {posicion} ")
else:
    print(f"el numero {buscar} no se puede encontrar en la array ")
    