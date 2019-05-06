#!/usr/bin/env python
#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
# from progress.bar import Bar
# from tqdm import tqdm

def Scraping(url, atributo):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html') # Creamos el objeto soup y le pasamos lo capturado con request
    market = soup.find_all(atributo)
    return market

def depurar(Lista, IniIter, ContenidoFinal, agregar):
    ListaDepurada = list()
    while Lista[IniIter] != ContenidoFinal:
        if (agregar == None) and (Lista[IniIter] != ''):
            ListaDepurada.append(Lista[IniIter])  # Lista depurada
        if (agregar != None) and (Lista[IniIter] != ''):
            ListaDepurada.append(agregar + Lista[IniIter])  # Lista depurada con agregado
        IniIter += 1
    return ListaDepurada

def libro(url, categoria):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        data = r.text
        soup = BeautifulSoup(data, 'html')  # Creamos el objeto soup y le pasamos lo capturado con request
        titulo = soup.find_all('h1')
        informacion = soup.find_all('td')
        description = soup.find_all('p')
        img = soup.find_all('img')
        UrlImg = 'http://books.toscrape.com' + img[0].get('src')[5:] # Url de la imagen
        Category = categoria
        Title = titulo[0].text
        Thumbnail = UrlImg
        Price = informacion[2].text[1:]
        Stock = re.findall('\d+',informacion[5].text.strip())
        Stock = int(Stock[0])
        Product = informacion[1].text
        Description = description[3].text
        upc = informacion[0].text
        json = {
            'category': Category,
            'title': Title,
            'thumbnail': Thumbnail,
            'price': Price,
            'stock': Stock,
            'product': Product,
            'description': Description,
            'upc': upc
            }
        return (json)
    else:
        print('Algo va mal, codigo de respuesta' + r.status_code)
        return

def scraper():
    json = []
    categorias = []
    LinkCategorias = []
    for link in Scraping(url= "http://books.toscrape.com/catalogue/category/books_1/index.html", atributo= 'a'):
        LinkCategorias.append(link.get('href')[2:])
        categorias.append(link.text.strip())

    categorias = depurar(Lista= categorias, IniIter= 3, ContenidoFinal= 'A Light in the ...', agregar=None)
    LinkCategorias = depurar(Lista= LinkCategorias, IniIter= 3, ContenidoFinal= '/../a-light-in-the-attic_1000/index.html', agregar='http://books.toscrape.com/catalogue/category')
    list_categorias = [{"id" : id_c+1 ,"name" : categoria} for id_c, categoria in enumerate(categorias)]
    json.append(list_categorias)
    list_libros = []
    for cnt, url in enumerate(LinkCategorias):
        i = 0
        for link in Scraping(url,'a'):
            if i > 53 and i % 2 == 0:
                if link.get('href') == 'page-2.html':
                    Urlpag = 'http://books.toscrape.com/catalogue/category/books/' + categorias[cnt].lower() + '_' + str(cnt + 2) + '/' + (link.get('href'))
                    Urlpag = Urlpag.replace(' ','-')
                    e = 0
                    for l in Scraping(url=Urlpag, atributo='a'):
                            if (e > 53) and (e % 2 == 0):
                                url2='http://books.toscrape.com/catalogue' + (l.get('href')[8:])
                                if url2 != 'http://books.toscrape.com/cataloguetml':
                                    libro(url2, cnt +1 )
                            e += 1
                else:
                    UrlLibro = 'http://books.toscrape.com/catalogue' + (link.get('href')[8:])
                    list_libros.append(libro(UrlLibro,cnt+1))
            i += 1
    
    json.append(list_libros)
    return json                  