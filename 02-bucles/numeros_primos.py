"""
Crea un programa que imprima todos los números primos entre el 2 y el 100. Un número primo es
un número positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo.
"""

# --- NÚMEROS PRIMOS ---
# Recorremos todos los números del 2 al 100
for num in range(2, 101):
    es_primo = True

    # Probamos si algún número entre 2 y num - 1 lo divide exactamente
    for divisor in range(2, num):
        if num % divisor == 0:
            es_primo = False
            break

    # Mostramos solo los que resultaron primos
    if es_primo:
        print(num)
