"""
3. Encuentre el segundo número más grande de una lista.
"""

# --- SEGUNDO NÚMERO MÁS GRANDE ---

# Creamos la lista
numeros = [45, 67, 100, 10, 12]

if len(numeros) < 2:
    print("La lista necesita al menos dos números.")
else:
    # Ordenamos de mayor a menor
    numeros.sort(reverse=True)

    # El segundo elemento es el segundo más grande
    print(numeros[1])
