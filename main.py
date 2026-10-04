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


##########################################################
# Ejercicio 2 — Conversión de tipos
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese su altura: ")

edad = int(edad)
altura = float(altura)

print(nombre)
print(edad)
print(altura)

print(type(nombre))
print(type(edad))
print(type(altura))


##########################################################
# Ejercicio 3 — Operaciones matemáticas
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

num1 = float(num1)
num2 = float(num2)

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
resto = num1 % num2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Resto:", resto)


##########################################################
# Ejercicio 4 — Mayor de edad
edad = input("Ingrese su edad: ")
edad = int(edad)

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


##########################################################
# Ejercicio 5 — Número positivo, negativo o cero
numero = input("Ingrese un número: ")
numero = float(numero)

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")


##########################################################
# Ejercicio 6 — Lista de números
numeros = [10, 25, 8, 40, 15, 30]

print(numeros)
print(numeros[0])
print(numeros[-1])
print(len(numeros))


###########################################################
# Ejercicio 7 — Recorrer una lista de nombres
nombres = ["Ana", "Pedro", "Laura", "Juan", "Sofía"]

for nombre in nombres:
    print(nombre)


#############################################################
# Ejercicio 8 — Notas aprobadas y desaprobadas
notas = [8, 4, 6, 10, 3, 7, 5]

for nota in notas:
    if nota >= 6:
        print(nota, "- Aprobada")
    else:
        print(nota, "- Desaprobada")


#################################################################
# Ejercicio 9 — Contar hasta un número
numero = input("Ingrese un número: ")
numero = int(numero)

for i in range(1, numero + 1):
    print(i)
