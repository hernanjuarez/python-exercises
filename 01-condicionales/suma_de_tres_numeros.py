"""
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
de los otros dos.
"""

# --- COMPARAR NÚMEROS ---
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Comprobamos si alguno es la suma de los otros dos
if num1 == num2 + num3:
    print("El primero es la suma del segundo con el tercero.")
elif num2 == num1 + num3:
    print("El segundo es la suma del primero con el tercero.")
elif num3 == num1 + num2:
    print("El tercero es la suma del primero con el segundo.")
else:
    print("Ninguno de los 3 números ingresados es la suma de los otros 2.")
