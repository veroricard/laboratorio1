def pedir_edad():
    edad = int(input("coloque edad: "))
    return edad


def pedir_altura():
    altura = float(input("coloque altura: "))
    return altura


def pedir_nombre():
    nombre = input("coloque nombre: ")
    return nombre


def pedir_ciudad():
    ciudad = input("coloque ciudad: ")
    return ciudad


dato1 = pedir_nombre()
dato2 = pedir_edad()
dato3 = pedir_altura()
dato4 = pedir_ciudad()

print("resultados")
print(f"nombre:{dato1},edad: {dato2},altura:{dato3},ciudad:{dato4}")


##############################################################################
# Ejercicio 1 — Datos personales
nombre = "Ana"
edad = 28
ciudad = "Cipolletti"
altura = 1.65

print(nombre)
print(edad)
print(ciudad)
print(altura)

print(type(nombre))
print(type(edad))
print(type(ciudad))
print(type(altura))
