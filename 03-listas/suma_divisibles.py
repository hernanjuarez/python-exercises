"""
5. Suma de los números de una lista que son divisibles por el número ingresado por el usuario.
"""

# --- SUMA DE NÚMEROS DIVISIBLES ---

# Lista de números
numeros = [4, 7, 8, 9, 3, 12, 45, 16, 90]

# Acumulador de resultados
resultado = 0

numero_ingresado = int(input("Ingrese un número: "))

if numero_ingresado == 0:
    print("Error: no se puede ingresar 0.")
else:
    # Recorremos la lista y sumamos los que son divisibles
    for num in numeros:
        if num % numero_ingresado == 0:
            resultado += num

    # Mostramos el resultado
    print(f"La suma de los números divisibles por {numero_ingresado} es: {resultado}")
