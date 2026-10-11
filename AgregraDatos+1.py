contador=0
números=[]
figuras=()
letras=set()
medidas={}
while contador<5:
    número=int(input("ingresa un numero a tu lista: "))
    números.append(número)
    figura=str(input("ingresa una figura a tu tupla: "))
    figuras+=(figura,)
    letra=str(input("ingresa una letra a tu conjunto: "))
    letras.add(letra)
    medida=str(input("ingresa una medida a tu diccionario: "))
    unidad=str(input("ingresa la unidad a tu diccionario: "))
    medidas[medida]=unidad
    contador=contador+1
print(números)
print(figuras)
print(letras)
print(medidas)
