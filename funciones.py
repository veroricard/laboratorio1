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
