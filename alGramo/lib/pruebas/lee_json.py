import json
archivo = raw_input("Ingrese ubicacion del json: ")
leer = json.loads(open(archivo).read())
mostrar = raw_input("Ingrese dato a consultar: ")

for i in range(7001):
	print leer[i][mostrar]