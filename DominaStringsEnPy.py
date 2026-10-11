print ("INDICES EN STRINGS")
texto = "Este es el texto"
print (texto[0])
print (texto[4])
print ("======================================")
print ("SLICING")
texto = "Este es el texto"
print (texto[0:4])
print (texto[ :7])
print (texto[5: ])
print (texto[5:-2])
print ("======================================")
print ("REEMPLAZAR TEXTO")
curso = "Este curso es de JavaScript"
print (curso.replace("JavaScript", "Python"))
print ("======================================")
print ("DIVIDIR TEXTO")
texto = "Este es el texto"
texto_dividido = texto.split(" ")
print (texto_dividido)
print ("======================================")
texto2 ="Este texto tiene MAYUSCULAS y minusculas"
buscado = "mayusculas"
print (buscado in texto2)
print (buscado.lower() in texto2.lower()) 
