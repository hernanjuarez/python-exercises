"""
Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
al mes. Además los tramos impositivos de la renta anual son los siguientes:
RENTA TIPO IMPOSITIVO
Menos de 15.000 eu 5%
Entre 15.000 y 25.000 eu 15%
Entre 25.000 y 35.000 eu 20%
Entre 35.000 y 60.000 eu 30%
Más de 60.000 eu 45%
Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.
"""

# --- TRIBUTO ---
edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo mensual en euros: € "))

# Requisitos para tributar: mayor de edad y más de 1000 euros al mes
if edad >= 18 and sueldo > 1000:
    print("Eres susceptible de tributar.")

    renta_anual = sueldo * 12

    # Cada tramo incluye su límite inferior; el de 35.000 a 60.000 incluye también el 60.000
    if renta_anual < 15000:
        print("Tu tipo impositivo es del 5%.")
    elif 15000 <= renta_anual < 25000:
        print("Tu tipo impositivo es del 15%.")
    elif 25000 <= renta_anual < 35000:
        print("Tu tipo impositivo es del 20%.")
    elif 35000 <= renta_anual <= 60000:
        print("Tu tipo impositivo es del 30%.")
    else:
        print("Tu tipo impositivo es del 45%.")

# No cumple los requisitos
else:
    print("No eres susceptible de tributar.")
