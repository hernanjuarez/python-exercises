"""
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
pantalla.
"""

# --- COMPARAR NÚMEROS ---
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

# Partimos suponiendo que el mayor es el primero
mayor = num1

# Comparamos con cada número y nos quedamos con el más grande
if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

if num4 > mayor:
    mayor = num4

print(f"El mayor de los 4 números es: {mayor}")
