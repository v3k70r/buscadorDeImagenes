import commands

#Obtiene todos los nombres de las imagenes ya descargadas

#directorio = raw_input("Ingrese directorio a listar: ")
mostrar = commands.getoutput('ls /home/valbarran/Desktop/AlGramo/images')
separado = mostrar.split(".")
separado.remove(separado[0])
descargadas = []
for i in range(len(separado)):
	descargadas.append(separado[i].split('\n'))
	#print codigo[i]

descargadas.remove(descargadas[0])
descargadas.pop()

#obtiene todos los codigos de productos de los archivos en el json

import json

archivo = '/home/valbarran/Desktop/AlGramo/Products.json'
leer = json.loads(open(archivo).read())
mostrar = 'EAN'
codigos_de_productos = []

for i in range(len(leer)):
	codigos_de_productos.append(leer[i][mostrar])
	#print codigos_de_productos[i]

#Crea una lista con los codigos de productos para fulturo filtrado con las imagenes existentes para generar la diferencia con las faltantes

faltantes = []
for i in range(len(codigos_de_productos)):
	faltantes.append(codigos_de_productos[i])

#saca de la lista "faltantes" si el producto esta en la lista de archivos ya descargados

for i in range(len(descargadas)):
	for j in range(len(codigos_de_productos)):
		if (codigos_de_productos[j] == descargadas[i][1]):
			faltantes.remove(descargadas[i][1])

#Mostrar resultado final de imagenes faltantes
for i in range(len(faltantes)):
	print faltantes[i]