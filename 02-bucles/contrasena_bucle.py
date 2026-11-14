"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

# --- CONTRASEÑA ---
# Contraseña de ejemplo (solo para practicar, no usar una real)
password = "python123"

# Empezamos con un valor vacío para que el bucle arranque
password_ingresada = ""

# Repetimos hasta que la contraseña ingresada sea la correcta
while password_ingresada != password:
    password_ingresada = input("Ingrese la contraseña: ")

    if password_ingresada != password:
        print("Contraseña incorrecta, intente nuevamente.")

print("¡Bienvenido!")
