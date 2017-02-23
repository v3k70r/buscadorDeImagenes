# -*- coding: utf-8 -*-
import json
import sys
import scraper
import os

def generarDirectorio(query,ruta):
  anteDirectorio = ruta
  directorio = anteDirectorio + query
  if not(os.path.exists(directorio)): 
    os.makedirs(directorio)
  return directorio

dirJson = raw_input("Ingrese la ruta del archivo JSon a cargar: ")
busqueda = json.loads(open(dirJson).read())
cd = raw_input("Desea crear un directorio?(si/no): ")
if cd == 'si':
  ruta = raw_input("Ingrese ruta donde se creara el directorio. (Ejmplo: /home/valbarran): ")
  ruta += '/'
  carpeta = raw_input("Ingrese nombre del directorio a crear: ")
  directorio = generarDirectorio(carpeta,ruta)
elif cd == 'no':
  directorio = raw_input("Ingrese directorio en el cual quiere que se descargen las imagenes: ")
else:
  print "Opcion no valida"
  print "Fin de la ejecucion."
  break
orden = 0 #Por defecto este script descarga el primer resultado de google imagenes
campo = raw_input("Ingrese nombre del campo del json el cual sera su busqueda: ")
for i in range(len(busqueda)):
  query = busqueda[i][campo]
  print query
  guardarComo = busqueda[i][campo]
  scraper.scrapear(query,guardarComo,directorio,orden) #manda la consulta al scraper

