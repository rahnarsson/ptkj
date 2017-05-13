from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Heippa! PTKJ RY:n kisasivusto.")


def detail(request, kilpailu_id):
    return HttpResponse('Vilkuilet PTKJ:n kisaa: {}'.format(kilpailu_id))


def add_lajipisteet(request, lajipisteet_id):
    return HttpResponse('Aseta lajipisteet: {}'.format(lajipisteet_id))
