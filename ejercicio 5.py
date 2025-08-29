def es_par(numero):
    return numero % 2 == 0

num = int(input("ingrese un numero: "))

if es_par(num):
    print(f"El numero {num} es par. ")
else: 
    print(F"El numero {num} es impar. ")
    
