"""
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla.
"""

# --- CONTRASEÑA SEGURA ---
password = input("Ingrese una contraseña: ")

# Requisitos
tiene_vocal = any(letra in "aeiou" for letra in password)
tiene_simbolos = "*" in password and "#" in password

if tiene_vocal and tiene_simbolos:
    print("La contraseña ingresada es segura.")
else:
    print("La contraseña ingresada es insegura.")
