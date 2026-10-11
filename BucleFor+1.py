# break: terminar el juego
for nivel in range(1, 6):
    if nivel == 4:
        break
print("Nivel completado:", nivel)
# continue: saltar una moneda
for moneda in range(1, 6):
    if moneda == 3:
        continue
print("Moneda recogida:", moneda)
