videojuego = {
"nombre": "Minecraft",
"categoria": "Aventura",
"precio": 599.90
}
# Acceder
print(videojuego["nombre"])
# Agregar / modificar
videojuego["plataforma"] = "PC"
videojuego["precio"] = 499.90
# Recorrer
# CLAVE Y VALOR
for clave, valor in videojuego.items():
    print(f"{clave}: {valor}")
# Valores
for valor in videojuego.values():
    print(valor)
# Claves
for clave in videojuego:
    print(clave)
