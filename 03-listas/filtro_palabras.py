"""
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida.
"""

# --- FILTRO DE PALABRAS ---

# Lista de palabras
palabras_random = ["fino", "elegante", "gato", "corneta", "Sol"]

# Lista de letras prohibidas
letras_prohibidas = ["g", "l", "e"]

# Lista vacía donde guardaremos las palabras que NO tienen letras prohibidas
palabras_filtradas = []

# Recorremos las palabras
for palabra in palabras_random:
    incluir = True

    # Comprobamos si la palabra tiene alguna letra prohibida
    for letra in letras_prohibidas:
        if letra in palabra.lower():
            incluir = False
            break

    # Si no tiene ninguna letra prohibida, la agregamos a la lista filtrada
    if incluir:
        palabras_filtradas.append(palabra)

# Mostramos los resultados
print("La lista original de palabras es:", palabras_random)
print("Las letras prohibidas son:", letras_prohibidas)
print("Las palabras que no contienen las letras prohibidas son:", palabras_filtradas)
