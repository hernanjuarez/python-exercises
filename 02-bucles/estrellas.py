"""
1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.
(Estructura: las estrellas aumentan hasta el número ingresado y luego disminuyen.)
"""

# --- ESTRELLAS ---
estrellas = int(input("Ingrese un número entero: "))

if estrellas < 1:
    print("Ingrese un número mayor a 0.")
else:
    # Parte ascendente: de 1 hasta el número ingresado
    for i in range(1, estrellas + 1):
        print("*" * i)

    # Parte descendente: desde el número menos uno hasta 1
    for i in range(estrellas - 1, 0, -1):
        print("*" * i)
