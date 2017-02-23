import json
import lib.scraper as scraper
import sys
import os

#Descarga una imagen en base a una consulta y la guarda en una ruta especificada
def generarDirectorio(query,ruta):
	anteDirectorio = ruta
	directorio = anteDirectorio + query
	if not(os.path.exists(directorio)): 
		os.makedirs(directorio)
	return directorio

query = raw_input("Ingrese su busqueda: ")
ruta = raw_input("Ingrese ruta donde descargar. (Ejemplo, /home/valbarran):")
ruta = ruta + '/'
cantidad = raw_input("Ingrese cantidad de imagenes a descargar: ")
rutaDirectorio = generarDirectorio(query, ruta)
cantidad = int(cantidad)
orden = 0 #El orden se refiere a cual resultado, de una lista de resultados del 0 al 99 desea descargar, por defecto descarga el primer resultado, osea el numero 0
for i in range(cantidad):
    scraper.scrapear(query, (i + 1), rutaDirectorio, i)