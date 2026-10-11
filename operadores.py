num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicacion:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("No se puede dividir entre cero")
