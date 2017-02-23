# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json
import urllib2

def scrapear(query, guardarComo, directorio, orden): #Obtiene la consulta, el nombre con que se guardará el archivo, y la carpeta donde se guardaran y los manda a los procesos de obtener links y obtener imagenes
	links = obtenerLinks(query)#Obtiene 100 links de imagenes resultado a la consulta a google imagenes segun el nombre del producto
	indice = orden #Es numero desde donde se comenzaran a descargar las imagenes
	#Comienza a intentar descargar una imagen del producto actual
	while indice < len(links):
		#En cuanto logra descargar una imagen con exito del producto actual se termina el proceso, sino, sigue intentando con otro link
		if(obtenerImagen(directorio,guardarComo,links[indice])):
			break
		else:
			indice =+ 1

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def obtenerLinks(query):#obtiene el link segun la consulta realizada
	image_type="ActiOn"
	query= query.split()
	query='+'.join(query)
	url="https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
	print url
	header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
	}
	soup = get_soup(url,header)
	links=[]
	for a in soup.find_all("div",{"class":"rg_meta"}):
		link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
		links.append((link,Type))
	return links

def obtenerImagen(directorio,guardarComo,link): #segun el link que recibe de la lista descarga la imagen y la guarda en la ruta especificada 
	URL = link[0]
	Type = link[1]
	print URL
	print Type
	print guardarComo
	print ""
	try:
		header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
		req = urllib2.Request(URL, headers={'User-Agent' : header})
		raw_img = urllib2.urlopen(req).read()
		if len(Type)==0:
			f = open(os.path.join(directorio , str(guardarComo)+".jpg"), 'wb')
		else:
			f = open(os.path.join(directorio , str(guardarComo)+"."+Type), 'wb')
			f.write(raw_img)
			f.close()
		return 1
	except Exception as e:
		print e
		return 0