def buscar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3: 
            return [num1, num2, num3]
        else: 
            return[num1, num3, num2]
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            return [num2, num1, num3]
        else: 
            return [num2, num3, num1]
    else: 
        if num1 >= num2:
            return [num3, num1, num2]
        else: 
            return [num3, num2, num1]

a = int(input("ingrese el primer numero: "))
b= int(input("ingrese el segundo numero: "))
c= int(input("ingrese el tercer numero: "))

orden = buscar_mayor(a, b, c)
print("Numeros ordenados de mayor a menor:", orden)
