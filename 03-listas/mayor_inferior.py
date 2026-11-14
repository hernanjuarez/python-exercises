"""
6. Pide un número y encuentra el número más alto de la lista que sea inferior al ingresado.
"""

# --- MAYOR NÚMERO INFERIOR AL INGRESADO ---

num_ingresado = int(input("Ingrese un número: "))

# Lista de números
numeros = [29, 38, 1, 92, 73, 48, 16, 28, 84, 1, 3, 4, 56, 7]

# Los ordenamos de menor a mayor
numeros.sort()

# Empezamos sin resultado, por si ningún número cumple
resultado = None

# El último que sea menor al ingresado es el más alto de los menores
for num in numeros:
    if num < num_ingresado:
        resultado = num

if resultado is None:
    print("Ningún número de la lista es inferior al ingresado.")
else:
    print(f"El número más alto inferior a {num_ingresado} es: {resultado}")
