# Trabajo Práctico Funciones

##########################################################
# Ejercicio 1 — Suma de dos números (se usan en el orden en que se pasan)

# Función nombrada
def suma(a, b):
    return a + b

# Función anónima
suma_lambda = lambda a, b: a + b

print("Ejercicio 1")
print(suma(3, 5))
print(suma_lambda(3, 5))


##########################################################
# Ejercicio 2 — Resta indicando explícitamente primero y segundo

# Función nombrada (el * obliga a usar los nombres al llamarla)
def resta(*, primero, segundo):
    return primero - segundo

# Función anónima
resta_lambda = lambda *, primero, segundo: primero - segundo

print("Ejercicio 2")
print(resta(primero=10, segundo=3))
print(resta_lambda(segundo=3, primero=10))


##########################################################
# Ejercicio 3 — Precio final con IVA (por defecto 21%)

# Función nombrada
def precio_final(precio, iva=21):
    return precio * (1 + iva / 100)

# Función anónima
precio_final_lambda = lambda precio, iva=21: precio * (1 + iva / 100)

print("Ejercicio 3")
print(precio_final(1000))
print(precio_final(1000, 10.5))
print(precio_final_lambda(1000))
print(precio_final_lambda(1000, 10.5))


##########################################################
# Ejercicio 4 — Convertir metros a otra unidad (por defecto centímetros)

# Función nombrada
def convertir_metros(metros, unidad="cm"):
    factores = {"cm": 100, "mm": 1000}
    return metros * factores[unidad]

# Función anónima
convertir_metros_lambda = lambda metros, unidad="cm": metros * {"cm": 100, "mm": 1000}[unidad]

print("Ejercicio 4")
print(convertir_metros(2))
print(convertir_metros(2, "mm"))
print(convertir_metros_lambda(2))
print(convertir_metros_lambda(2, "mm"))
