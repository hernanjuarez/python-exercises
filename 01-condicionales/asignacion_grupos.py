"""
En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
pantalla el grupo que le corresponde a ese alumno.
"""

# --- ASIGNACIÓN DE GRUPOS ---
genero = input("Ingrese el género (chico/chica): ").strip().lower()
nombre = input("Ingrese su nombre: ").strip()

if nombre == "":
    print("Error: no ingresó ningún nombre.")
elif genero == "chica":
    inicial = nombre[0].upper()
    # Chicas: de la E a la M van al grupo A
    if "E" <= inicial <= "M":
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")
elif genero == "chico":
    inicial = nombre[0].upper()
    # Chicos: de la A a la H y de la R a la Z van al grupo A
    if "A" <= inicial <= "H" or "R" <= inicial <= "Z":
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")
else:
    print("Género mal ingresado.")
