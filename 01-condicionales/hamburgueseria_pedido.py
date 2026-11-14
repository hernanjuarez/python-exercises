"""
En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
Los ingredientes extra de la hamburguesa clásica son:
- Queso Idiazabal
- Bacon
- Huevo
Los ingredientes extra de la hamburguesa vegana son:
- Tofu
- Cebolla caramelizada
Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la
respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos.
Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus
ingredientes
"""

# --- HAMBURGUESERÍA ---
extras_clasica = ["queso idiazabal", "bacon", "huevo"]
extras_vegana = ["tofu", "cebolla caramelizada"]

tipo = input("Ingrese el tipo de hamburguesa (clasica/vegana): ").strip().lower()

if tipo == "clasica":
    extras = extras_clasica
elif tipo == "vegana":
    extras = extras_vegana
else:
    extras = None
    print("Las hamburguesas disponibles son clasica y vegana.")

if extras is not None:
    print("Extras disponibles:", ", ".join(extras))
    extra = input("Elija un ingrediente extra: ").strip().lower()

    if extra in extras:
        print(f"Hamburguesa elegida: {tipo} con extra de {extra}.")
    else:
        print("Ingrediente extra mal ingresado.")
