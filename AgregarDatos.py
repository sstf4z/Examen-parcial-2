#ejemplos lista, tupla, conjunto, diccionario
#todos almacenan datos, pero funcionan de forma distinta, 
#su principal distintivo es la forma en que almacenan los datos
#y la forma en que se agregan los mismos

print("ejemplo lista")
compras=["pan", "leche"]
compras.append("huevos")
print(compras)

print("ejemplo tupla")
ubicación=("casa", "trabajo")
ubicación+=("escuela",)
print(ubicación)

print("ejemplo conjunto")
categorias={"comida", "bebida"}
categorias.add("limpieza")
print(categorias)

print("ejemplo diccionario")
precios={"pan":25}
precios["leche"]=30
print(precios)
