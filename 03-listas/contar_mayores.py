"""
3. Contar los números más grandes que el ingresado por el usuario.
"""

# --- CONTAR NÚMEROS MÁS GRANDES ---

# Creamos la lista
numeros = [1, 100, 59, 36, 85, 18, 29, 40, 28, 17, 37, 84, 73, 92]

ingresado = int(input("Ingrese un número: "))
contador = 0

# Contamos cuántos números de la lista son mayores que el ingresado
for num in numeros:
    if num > ingresado:
        contador += 1

print(f"Hay {contador} números mayores que {ingresado} en la lista.")
