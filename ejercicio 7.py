def verificar_acceso(edad):
    if edad >= 18:
        return True
    else:
        return False

edad_usuario = int(input("Ingrese su edad: "))

if verificar_acceso(edad_usuario):
    print("Acceso permitido. Sos mayor de edad.")
else:
    print("Acceso denegado. Sos menor de edad.")

