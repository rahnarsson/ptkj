from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse


from .models import Kilpailu, Kisaaja


def index(request):
    kisalista = Kilpailu.objects.order_by('vuosi')
    objects = ', '.join([k.nimi for k in kisalista])
    template = loader.get_template('kisa/index.html')
    context = {
        'kisalista': kisalista,
    }
    return HttpResponse(template.render(context, request))


def detail(request, kilpailu_id):
    return HttpResponse('Vilkuilet PTKJ:n kisaa: {}'.format(kilpailu_id))


def lisaa_kisaaja(request):

    template = loader.get_template('kisa/lisaa_kisaaja.html')
    if request.method == 'POST':
        uusi_kisaaja = Kisaaja(nimi_etu=request.POST['nimi_etu'], nimi_suku=request.POST['nimi_suku'], ruoka_allergiat=request.POST['allergiat'])
        # uusi_kisaaja['nimi_etu'] = request.POST['nimi_etu']
        # uusi_kisaaja['nimi_suku'] = request.POST['nimi_suku']
        # uusi_kisaaja['ruoka_allergiat'] = request.POST['allergiat']
        uusi_kisaaja.save()
        context = {}
        return HttpResponse(template.render(context, request))
    else:
        context = {}
        return HttpResponse(template.render(context, request))


def add_lajipisteet(request, lajipisteet_id):
    return HttpResponse('Aseta lajipisteet: {}'.format(lajipisteet_id))
