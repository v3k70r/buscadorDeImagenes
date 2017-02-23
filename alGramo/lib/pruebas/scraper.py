# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import requests #para las funcionalidades de HTTP
import re #para expresiones regulares
import urllib2 #para extraer una pagina web
import os #para el manejo de funcionalidades del sistema operativo
import cookielib #para el uso de cookie de las paginas del internet
import json #para el manejo de jsons
import urllib2

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def obtenerLinks(query):#En base a la consulta busca el link del primer resultado
	query = unicode(query, "utf-8")
	image_type="ActiOn"
	query= query.split()
	query='+'.join(query)
	url="https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
	header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
	}
	soup = get_soup(url,header)
	links=[]
	for a in soup.find_all("div",{"class":"rg_meta"}):
		link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
		links.append((link,Type))
	return links

def obtenerImagen(DIR,guardarComo,link):#en base al link obtenido, descarga la imagen y la guarda en la ruta
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
			f = open(os.path.join(DIR , str(guardarComo)+".jpg"), 'wb')
		else:
			f = open(os.path.join(DIR , str(guardarComo)+"."+Type), 'wb')
			f.write(raw_img)
			f.close()
		return 1
	except Exception as e:
		print e
		return 0

def scrapear(query,guardarComo,DIR):#recibe los datos desde el accesador y los envia a los "obtenerLinks" y "obtenerImagenes"
	links = obtenerLinks(query)
	indice = 0
	print len(links)
	while(indice < len(links)):
		if(obtenerImagen(DIR,guardarComo,links[indice])):
			break
		indice += 1

    


    