temperaturas={}
suma=0
for i in range(7):
    día=str(input("ingresa el día de la semana: "))
    temperatura=float(input("ingresa la temperatura: "))
    temperaturas[día]=temperatura
    suma+=temperatura
promTem=suma/7
valMax=max(temperaturas.values())
valMin=min(temperaturas.values())
print("el promedio de temperaturas semanal fue de: ",promTem )
print("la temperatura más alta de la semana fue: ",valMax )
print("la temperatura más baja de la semana fue: ",valMin )
