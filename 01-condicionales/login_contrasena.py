"""
LOG-IN:
Crea un script que pida una contraseña al usuario (el script sabe cuál es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.
"""

# --- VALIDAR CONTRASEÑA ---
# Contraseña de ejemplo (solo para practicar, no usar una real)
password_correcta = "python123"

# Primer intento
password_ingresada = input("Ingrese su contraseña: ")

if password_ingresada.lower() == password_correcta.lower():
    print("Contraseña correcta. ¡Bienvenido!")
else:
    # Contraseña incorrecta: damos un segundo intento
    print("Contraseña incorrecta. Le queda 1 intento más.")
    password_ingresada = input("Ingrese su contraseña nuevamente: ")

    if password_ingresada.lower() == password_correcta.lower():
        print("Contraseña correcta. ¡Bienvenido!")
    else:
        print("Contraseña incorrecta.")
        print("No le quedan más intentos.")
