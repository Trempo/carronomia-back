import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

import scraping.utils as utils


def scrape(request, busqueda):
    carros = utils.scrape(busqueda)
    carros_dto = serializers.serialize('json', carros)
    return HttpResponse(carros_dto, 'application/json')


def stats(request, busqueda,year):
    carros = utils.scrape(busqueda)
    years, promedios, kms, prediccion = utils.promedioAnual(carros, year)
    localidades, numero = utils.carrosPorLocalidad(carros)
    respuesta = {
        'promedioAnual': {
            'years': years,
            'promedios': promedios,
            'kms': kms
        },
        'numeroPorLocalidad': {
            'localidad': localidades,
            'numero': numero
        },
        'prediccion': prediccion[0],

    }
    return HttpResponse(json.dumps(respuesta, indent=4), 'application/json')


