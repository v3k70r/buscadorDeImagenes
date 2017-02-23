# -*- coding: utf-8 -*-
import json
import lib.scraper as scraper
import sys

def main():
    productos = json.loads(open('/home/valbarran/Desktop/AlGramo/Products.json').read()) #el archivo "Products.json" debe estar junto al script
    directorio = "/home/valbarran/Desktop/AlGramo/images/"
    inicial = sys.argv[1] #al ejecutar el script se agrega un argumento que es el numero del producto(en orden) desde el cual se empiezan a descargar las imagenes
    orden = 0 #Por defecto este script descarga el primer resultado de google imagenes
    inicial = int(inicial)
    for i in range(inicial, len(productos)):
    	print leer[i]['Product']
   		query = str(leer[i]['Product'])
   		guardarComo = str(leer[i]['EAN'])
   		scraper.scrapear(query,guardarComo,directorio,orden) #manda la consulta al scraper

if __name__ == "__main__":
    main()
	
