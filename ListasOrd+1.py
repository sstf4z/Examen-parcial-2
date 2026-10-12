frutas = ["Manzana", "Pera", "Uva"]
precios = [15.0, 20.0, 12.5]

print(frutas[0]) # "Manzana"
print(frutas[-1]) # "Uva"

frutas.append("Mango")
frutas.remove("Pera")
# Longitud
print(len(frutas)) # 3
# Recorrer
for f in frutas:
    print(f)
