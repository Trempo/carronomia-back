from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

import scraping.utils as utils


def scrape(request, busqueda):
    carros = utils.scrape(busqueda)
    carros_dto = serializers.serialize('json', carros)
    return HttpResponse(carros_dto, 'application/json')


def promedio(request, busqueda):
    carros = utils.scrape(busqueda)
    promedio = utils.promedioPreciosAnual(carros)
    return HttpResponse(promedio, 'application/json')


def home(request):
    return render(request, 'index.html')
