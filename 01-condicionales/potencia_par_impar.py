"""
Crea un script que dado un número y una potencia compruebe si ese número elevado a esa
potencia es par o impar.
"""

# --- NÚMERO ELEVADO A UNA POTENCIA: ¿PAR O IMPAR? ---
numero = int(input("Introduzca un número: "))
potencia = int(input("Introduzca la potencia: "))

resultado = numero ** potencia

if resultado % 2 == 0:
    print(f"{numero} elevado a {potencia} es {resultado}, y es par.")
else:
    print(f"{numero} elevado a {potencia} es {resultado}, y es impar.")
