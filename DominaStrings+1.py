print ("SLICING")
texto = "Este es el texto que se va a utilizar para el ejemplo"
print (texto[0:9])
print (texto[ :15])
print (texto[16: ])
print (texto[16:-3])
print ("======================================")
print ("REEMPLAZAR TEXTO")
curso = "Los Lunes y jueves tengo clase de etica"
print (curso.replace("etica", "ingles"))
print ("======================================")
print ("DIVIDIR TEXTO")
texto = "los fines de semana no hago nada"
texto_dividido = texto.split(" ")
print (texto_dividido)
print ("======================================")
texto2 ="Yo Si sE esCribIr biEN"
buscado = "mayusculas"
print (buscado in texto2)
print (buscado.lower() in texto2.lower())  
