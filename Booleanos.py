t= True 
f= False

print("ingresa un número")
num1 = int(input())
print("ingresa otro número")
num2 = int(input())

if num1 > num2:
    print( "El primer número es mayor que el segundo número")
    print("True")
else: 
    print("El primer número no es mayor que el segundo número")
    print("False")

if num1 < num2:
    print("El primer número es menor que el segundo número")
    print("True")
else:
    print("El primer número no es menor que el segundo número")
    print("False")  

if num1 == num2:
    print("El primer número es igual al segundo número")
    print("True")   
else: 
    print("El primer número no es igual al segundo número")
    print("False")
