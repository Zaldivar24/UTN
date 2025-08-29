def area_del_triangulo(base, altura):
    return(base * altura) / 2

b = float(input("Ingrese la base del triángulo: "))
a = float(input("Ingrese la altura del triángulo: "))

area = area_del_triangulo(b, a)
print("El área del triángulo es:", area)

