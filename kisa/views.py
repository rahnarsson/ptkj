from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import Kilpailu, Kisaaja

navigation_bar = [
  ['/kisa', 'index', 'Kisat'],
  ['/kisa/kisaajat', 'kisaajat', 'Kisaajat'],
  ['/kisa/lajit', 'lajit', 'Lajit']
]

def index(request):
    kisalista = Kilpailu.objects.order_by('vuosi')
    objects = ', '.join([k.nimi for k in kisalista])
    global navigation_bar
    template = loader.get_template('jinja2/index.html.j2')
    context = {
        'kisalista': kisalista,
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'index', 'name': 'Etusivu'}
    }
    return HttpResponse(template.render(context, request))


def detail(request, kilpailu_id):
    global navigation_bar
    template = loader.get_template('jinja2/kisa.html.j2')
    context = {
        'kisa': kilpailu_id,
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'kisa', 'name': 'Kisa'}
    }
    return HttpResponse(template.render(context, request))


def lisaa_kisaaja(request):
    global navigation_bar
    template = loader.get_template('jinja2/lisaa_kisaaja.html.j2')
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
    kisaajat = [{ 'name': 'Heidi Lehtonen'}, {'name': 'Antti Rahikainen'}]
    global navigation_bar
    template = loader.get_template('jinja2/osallistujat.html.j2')
    context = {
        'navigation_bar': navigation_bar,
        'kisa': { 'id': kilpailu_id, 'name': 'Kesäkisat 2017'},
        'kisaajalista': kisaajat,
        'active_page': { 'id': 'kisaajat', 'name': 'Kisa ' + kilpailu_id + ' > Kisaajat'}
    }
    return HttpResponse(template.render(context, request))


def kaikki_kisaajat(request):
    global navigation_bar
    template = loader.get_template('jinja2/kisaajat.html.j2')
    context = {
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'kisaajat', 'name': 'Kaikki kisaajat'}
    }

    return HttpResponse(template.render(context, request))


def kisaaja(request, kisaaja_id):
    template = loader.get_template('jinja2/kisaaja.html.j2')
    global navigation_bar
    context = {
        'navigation_bar': navigation_bar,
        'kisaaja_id': kisaaja_id,
        'active_page': { 'id': 'kisaaja', 'name': 'Kisaaja ' + kisaaja_id}
    }
    return HttpResponse(template.render(context, request))

def kisaajainfo(request, kisaaja_id):
    context = {}
    template = loader.get_template('jinja2/modals/kisaajainfo.html.j2')
    return HttpResponse(template.render(context, request))

def ilmoittaudu(request):
    template = loader.get_template('jinja2/ilmoittaudu.html.j2')
    context = {}
    return HttpResponse(template.render(context, request))

def lajit(request):
    template = loader.get_template('jinja2/lajit.html.j2')
    context = {
        'navigation_bar': navigation_bar,
        'active_page': { 'id': 'lajit', 'name': 'Lajit '}
    }
    return HttpResponse(template.render(context, request))

def lajityyppiinfo(request):
    template = loader.get_template('jinja2/lajityyppiinfo.html.j2')
    context = {}
    return HttpResponse(template.render(context, request))
