import json
import lib.scraper2 as scraper
import sys
import os

#Descarga una imagen en base a una consulta y la guarda en una ruta especificada
#AL ejecutar requiere dos argumentos, el primero es la consulta de imagenes a descargar y la segunda la ruta donde se guardara la imagen a descargar.
def generarDirectorio(query,ruta):
	anteDirectorio = ruta
	directorio = anteDirectorio + query
	if not(os.path.exists(directorio)): 
		os.makedirs(directorio)
	return directorio

def main():
    for arg in sys.argv[1:]:
        print arg
    query = sys.argv[1]
    ruta = sys.argv[2]
    cantidad = sys.argv[3]
    rutaDirectorio = generarDirectorio(query, ruta)
    cantidad = int(cantidad)
    print scraper.scrapear(query, rutaDirectorio, cantidad)

if __name__ == "__main__":
    main()

