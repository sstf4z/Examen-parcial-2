# break: salir del ciclo
for i in range(10):
    if i== 5:
        break
print(i) # 0,1,2,3,4
# continue: saltar iteración
for i in range(6):
    if i == 3:
        continue
print(i) # 0,1,2,4,5
