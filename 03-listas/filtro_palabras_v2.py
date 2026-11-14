"""
Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida.
"""

# --- FILTRO DE PALABRAS (VERSIÓN 2) ---

# Lista de palabras
lista_palabras = ["gato", "perro", "puerta", "mueble", "licuadora"]

# Lista de letras prohibidas (tres letras)
letras_prohibidas = ["g", "i", "p"]

# Lista vacía donde guardaremos las palabras filtradas
lista_palabras_filtrada = []

# Recorremos la lista de palabras
for palabra in lista_palabras:
    incluir = True

    # Recorremos la lista de letras prohibidas
    for letra in letras_prohibidas:
        # Si la letra está en la palabra, no la incluimos
        if letra in palabra.lower():
            incluir = False
            break

    # Si no tiene ninguna letra prohibida, la agregamos a la lista filtrada
    if incluir:
        lista_palabras_filtrada.append(palabra)

# Mostramos el resultado
print(lista_palabras_filtrada)
