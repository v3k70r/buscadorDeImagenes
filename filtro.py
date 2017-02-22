# -*- coding: utf8 -*-
import json
import commands
import sys
import lib.scraper as scraper

def main():
    ruta = sys.argv[1]#Ruta donde estan las imagenes
    trozoRuta = ruta.split("/")
    imagen = sys.argv[2]#imagen especifica a reemplazar
    orden = sys.argv[3]#cual resultado reemplazará al resultado anterior
    orden = int(orden)
    query = trozoRuta[len(trozoRuta) - 1]
    guardarComo = imagen
    print query
    #scraper.scrapear(query,guardarComo,ruta,orden)

if __name__ == "__main__":
    main()