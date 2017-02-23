# -*- coding: utf8 -*-
import json
import commands
import sys
import lib.scraper as scraper

#Lista las imagenes ya descargadas a filtrar de la carpeta especificada
listadoDeImagenes = commands.getoutput('ls /home/valbarran/Desktop/AlGramo/images/filtrar')#obtiene listadas en una misma cadena todas las imagenes a filtrar
listadoDeImagenes = listadoDeImagenes.split("\n")#Separa la lista recibida por imagen
#Separa por cada imagen el nombre de la extension
for i in range(len(listadoDeImagenes)):
	listadoDeImagenes[i] = listadoDeImagenes[i].split(".") 
#Obtiene los datos desde el JSon de productos
productos = json.loads(open('/home/valbarran/Desktop/AlGramo/Products.json').read())#Este es el archivo json que contiene los productos

def main():
    orden = sys.argv[1] #EL numero del resultado en un orden de 1 a 100 que desea descargar
    inicial = sys.argv[2] #numero en orden del producto desde el cual se desea realizar el scraping
    orden = int(orden)
    DIR = "/home/valbarran/Desktop/AlGramo/images/filtrar/filtradas1" #Este es el directorio donde se guardarán las nuevas imagenes
    descargar = []
    listadoDeImagenes.pop()#borra el ultimo elemento de la lista que vendria siendo la carpeta "filtradas1" por que no corrsponde a una imagen
    #Hace un match entre las imagenes ya descargadas y los productos para rescatar el nombre del producto y realizar una nueva busqueda
    for i in range(len(listadoDeImagenes)):
    	for j in range(len(productos)):
    		if (int(listadoDeImagenes[i][0]) == int(productos[j]['EAN'])):#compara los "EAN" que es el nombre de los archivos imagenes y en los productos el codigo
    			descargar.append([productos[j]['Product'], productos[j]['EAN'],])#Si encuentra el producto referido por el archivo de imagen, rescata el nombre y el EAN en una nueva lista
    #Realiza el scrapping desde el producto especificado en la variable "inicial" y descarga el resultado en orden a la variable "orden"
    for i in range(int(inicial), len(descargar)):
    	query = descargar[i][0]#La query o consulta a google imagenes sera el nombre del producto
    	guardarComo = descargar[i][1]#El nombre del archivo en el que se guardara la imagen corresponde al EAN del producto
    	scraper.scrapear(query,guardarComo,DIR,orden)

if __name__ == "__main__":
    main()