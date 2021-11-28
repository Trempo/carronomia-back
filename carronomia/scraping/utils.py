from bs4 import BeautifulSoup
from carros.models import Carro
import requests
import matplotlib.pyplot as plt
from collections import OrderedDict


def scrape(busqueda):
    URL = 'https://listado.tucarro.com.co/' + busqueda
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.find_all('div', class_='ui-search-result__wrapper')
    carros = []
    i = 1
    while len(divs) > 0:
        for div in divs:
            year = div.findChildren('li', class_='ui-search-card-attributes__attribute')[0].text
            km = div.findChildren('li', class_='ui-search-card-attributes__attribute')[1].text.replace('Km', '').replace('.', '').replace(' ', '')
            precio = div.findChildren('span', class_='price-tag-fraction')[0].text.replace('.', '')
            modelo = div.findChildren('h2', class_='ui-search-item__title')[0].text
            ciudad = div.findChildren('span', class_='ui-search-item__location')[0].text
            carro = Carro(modelo=modelo, precio=precio, year=year, km=km, ciudad=ciudad)
            carros.append(carro)

        param = 49 * i - i + 1
        URL = 'https://listado.tucarro.com.co/' + busqueda + '_Desde_' + str(param) + '_NoIndex_True#filter'
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        divs = soup.find_all('div', class_='ui-search-result__wrapper')
        i += 1

    return carros


#Graficar el precio de los carros por año usando matplotlib
def promedioPreciosAnual(carros):
    carros.sort(key=lambda x: x.year, reverse=False)
    years = [int(carro.year) for carro in carros]
    years.sort()
    promedios = []
    # Promedio de precios de carros por año
    for year in years:
        promedio = 0
        i=0
        for carro in carros:
            if int(carro.year) == year:
                promedio += int(carro.precio)
                i += 1
        if(i != 0):
            promedios.append(promedio/i)
    return tuple(OrderedDict.fromkeys(years).keys()), tuple(OrderedDict.fromkeys(promedios).keys())

def carrosPorLocalidad(carros):
    carros.sort(key=lambda x: x.ciudad, reverse=False)
    ciudades = [carro.ciudad for carro in carros]
    cantidad = []
    for ciudad in ciudades:
        cantidad.append(ciudades.count(ciudad))
    return tuple(OrderedDict.fromkeys(ciudades).keys()), tuple(OrderedDict.fromkeys(cantidad).keys())

