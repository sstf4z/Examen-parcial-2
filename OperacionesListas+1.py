precios = [25.0, 40.0, 15.0, 30.0, 20.0]
# Precio mayor, menor y suma
print(max(precios))
print(min(precios))
print(sum(precios))
# Promedio
prom = sum(precios) / len(precios)
print(prom)
# Orden ascendente
precios.sort()
print("De menor a mayor:", precios)
# Orden descendente
precios.sort(reverse=True)
print("De mayor a menor:", precios)
# Los primeros 3 precios
top3 = precios[:3]
print("Los 3 primeros:", top3)
