"""
1. Crea una lista llamada "numeros" que contenga los siguientes numeros enteros:
[1,2,3,4,5,6,7,8,9,10].
2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
3. Escribe un bucle que recorra la lista "numeros" e imprima el cuadrado de cada numero por
consola.
4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
compresión).
5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
6. Haz lo mismo con el número más alto
7. Suma todos los elementos de la lista con y sin un bucle.
8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
el punto 2
"""

# --- LISTA DE NÚMEROS ---

# 1. Creamos la lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Lista con los pares en orden inverso
numeros_pares = []
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
numeros_pares_reversa = numeros_pares[::-1]
print("Pares en orden inverso:", numeros_pares_reversa)
print("---------")

# 3. Cuadrado de cada número
for num in numeros:
    print(num ** 2)
print("---------")

# 4. Pasos 2 y 3 con listas por comprensión
numeros_pares_invertidos = [num for num in numeros if num % 2 == 0][::-1]
numeros_cuadrados = [num ** 2 for num in numeros]
print("Pares invertidos (comprensión):", numeros_pares_invertidos)
print("Cuadrados (comprensión):", numeros_cuadrados)
print("---------")

# 5. Número más pequeño
minimo = min(numeros)
print("El número más pequeño de la lista es:", minimo)
print("---------")

# 6. Número más grande
maximo = max(numeros)
print("El número más grande de la lista es:", maximo)
print("---------")

# 7. Suma de todos los elementos, sin y con bucle
suma = sum(numeros)
print("Suma sin bucle:", suma)

suma_bucle = 0
for num in numeros:
    suma_bucle += num
print("Suma con bucle:", suma_bucle)
print("---------")

# 8. Índice del 8 en la lista original y en la lista del punto 2
indice_8_original = numeros.index(8)
indice_8_pares_invertidos = numeros_pares_reversa.index(8)
print("Índice del 8 en la lista original:", indice_8_original)
print("Índice del 8 en la lista de pares invertidos:", indice_8_pares_invertidos)
