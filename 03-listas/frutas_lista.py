"""
1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa.
2. Usa la función len() para imprimir la longitud de la lista frutas.
3. Accede al objeto numero 3 de la lista e imprímelo or consola.
4. Modifica el segundo objeto de la lista y cambiado a mora.
5. Añade el string mango al final de la lista.
6. Usa el método insert() y añade el string "uva" al comienzo de la lista.
7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable
llamada "ultima_fruta"
9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola
11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que
tengan más de 5 caracteres
12. Usa el método remove() para borrar el string "cereza" de la lista.
13. Usa el método clear() para vaciar la lista.
Recomendación: En cada paso comprueba que el código hace aquello que quieres
"""

# --- FRUTAS ---

# 1. Lista de frutas
frutas = ["manzana", "plátano", "cereza", "pera", "higo", "frambuesa", "fresa"]

# 2. Cantidad de frutas
print(len(frutas))
print("------------")

# 3. Objeto número 3 de la lista (índice 2)
print(frutas[2])
print("------------")

# 4. Modificar el segundo objeto
frutas[1] = "mora"

# 5. Añadir mango al final
frutas.append("mango")

# 6. Añadir uva al comienzo
frutas.insert(0, "uva")

# 7. Mostrar todos los elementos uno a uno
for fruta in frutas:
    print(fruta)
print("------------")

# 8. Eliminar el último elemento y guardarlo
ultima_fruta = frutas.pop()
print(f"Fruta eliminada: {ultima_fruta}")
print("------------")

# 9. Mostrar todos los elementos uno a uno
for fruta in frutas:
    print(fruta)
print("------------")

# 10. Mostrar también la longitud de cada nombre
for fruta in frutas:
    print(f"La fruta {fruta} tiene longitud: {len(fruta)}")
print("------------")

# 11. Mostrar solo los nombres con más de 5 caracteres
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)
print("------------")

# 12. Eliminar "cereza" de la lista
frutas.remove("cereza")

# 13. Vaciar la lista
frutas.clear()
print(frutas)
