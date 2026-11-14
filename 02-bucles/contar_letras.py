"""
Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.
"""

# --- CONTAR LETRAS EN UNA FRASE ---
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

if len(letra) != 1:
    print("Debe ingresar exactamente una letra.")
else:
    contador = 0

    # Recorremos la frase y contamos las coincidencias (sin distinguir mayúsculas)
    for caracter in frase.lower():
        if caracter == letra.lower():
            contador += 1

    print(f"La letra '{letra}' aparece {contador} veces en la frase.")
