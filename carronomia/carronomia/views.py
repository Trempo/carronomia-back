import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

import scraping.utils as utils


def scrape(request, busqueda):
    carros = utils.scrape(busqueda)
    carros_dto = serializers.serialize('json', carros)
    return HttpResponse(carros_dto, 'application/json')


def stats(request, busqueda):
    carros = utils.scrape(busqueda)
    years, promedios = utils.promedioPreciosAnual(carros)
    localidades, numero = utils.carrosPorLocalidad(carros)
    respuesta = {
        'promedioAnual': {
            'years': years,
            'promedios': promedios,
        },
        'numeroPorLocalidad': {
            'localidad': localidades,
            'numero': numero
        }

    }
    return HttpResponse(json.dumps(respuesta, indent=4), 'application/json')


