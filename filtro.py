# -*- coding: utf8 -*-
import json
import commands
import sys
import lib.scraper as scraper
import os
import shutil

ruta = raw_input("Ingrese ruta donde estan las imagenes donde de estas usted quiere reemplazar una. (Ejemplo: /home/valbarran): ")#Ruta donde estan las imagenes
trozoRuta = ruta.split("/")
imagen = raw_input("Ingrese nombre de imagen a reemplazar(incluyendo extension): ")#imagen especifica a reemplazar
orden = raw_input("Ingrese en un orden del 0 al 99, cual es el numero del resultado que quiere descargar: ")#cual resultado reemplazará al resultado anterior
orden = int(orden)
query = trozoRuta[len(trozoRuta) - 1]
guardarComo = imagen.split(".")[0]
print guardarComo
os.remove(ruta + '/' + imagen)
scraper.scrapear(query,guardarComo,ruta,orden)