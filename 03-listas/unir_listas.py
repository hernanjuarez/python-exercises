"""
2. Unir dos listas y ordenarlas en orden ascendente.
"""

# --- UNIR Y ORDENAR LISTAS ---

# Creamos las listas
lista_1 = [1, 4, 8, 10, 12]
lista_2 = [90, 15, 12, 4, 5]

# Unimos las listas
lista_conjunto = lista_1 + lista_2

# Ordenamos la lista nueva (de menor a mayor)
lista_conjunto.sort()

# Mostramos el resultado
print(lista_conjunto)
