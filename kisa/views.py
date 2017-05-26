from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import Kilpailu, Kisaaja

navigation_bar = [
  ['/kisa', 'index', 'Kisat'],
  ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
]

def index(request):
    kisalista = Kilpailu.objects.order_by('vuosi')
    objects = ', '.join([k.nimi for k in kisalista])
    template = loader.get_template('kisa/index.html')
    global navigation_bar
    context = {
        'kisalista': kisalista,
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'index', 'name': 'Etusivu'}
    }
    return HttpResponse(template.render(context, request))


def detail(request, kilpailu_id):
    template = loader.get_template('kisa/kisa.html')
    global navigation_bar
    context = {
        'kisa': kilpailu_id,
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'kisa', 'name': 'Kisa'}
    }
    return HttpResponse(template.render(context, request))


def lisaa_kisaaja(request):
    global navigation_bar
    template = loader.get_template('kisa/lisaa_kisaaja.html')
    if request.method == 'POST':
        uusi_kisaaja = Kisaaja(nimi_etu=request.POST['nimi_etu'], nimi_suku=request.POST['nimi_suku'], ruoka_allergiat=request.POST['allergiat'])
        # uusi_kisaaja['nimi_etu'] = request.POST['nimi_etu']
        # uusi_kisaaja['nimi_suku'] = request.POST['nimi_suku']
        # uusi_kisaaja['ruoka_allergiat'] = request.POST['allergiat']
        uusi_kisaaja_id = uusi_kisaaja.save()
        return HttpResponseRedirect('/kisaaja/1')
        #return HttpResponse(template.render(context, request))
    else:
        context = {
            'navigation_bar': navigation_bar,
            'active_page': { 'id': 'lisaa_kisaaja', 'name': 'Lisää kisaaja'}
        }
        return HttpResponse(template.render(context, request))


def add_lajipisteet(request, lajipisteet_id):
    return HttpResponse('Aseta lajipisteet: {}'.format(lajipisteet_id))

def kisaajat(request, kilpailu_id):
    template = loader.get_template('kisa/kisaajat.html')
    global navigation_bar
    context = {
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'kisaajat', 'name': 'Kisa ' + kilpailu_id + ' > Kisaajat'}
    }
    return HttpResponse(template.render(context, request))

def kaikki_kisaajat(request):
    template = loader.get_template('kisa/kisaajat.html')
    global navigation_bar
    context = {
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'kisaajat', 'name': 'Kaikki kisaajat'}
    }
    return HttpResponse(template.render(context, request))


def kisaaja(request, kisaaja_id):
    template = loader.get_template('kisa/kisaaja.html')
    global navigation_bar
    context = {
        'navigation_bar': navigation_bar,
        'kisaaja_id': kisaaja_id,
        'active_page': { 'id': 'kisaaja', 'name': 'Kisaaja ' + kisaaja_id}
    }
    return HttpResponse(template.render(context, request))
