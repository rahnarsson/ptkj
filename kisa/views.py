from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse


from .models import Kilpailu, Kisaaja


def index(request):
    kisalista = Kilpailu.objects.order_by('vuosi')
    objects = ', '.join([k.nimi for k in kisalista])
    template = loader.get_template('jinja2/index.html.j2')
    context = {
        'kisalista': kisalista,
        'navigation_bar': [
          ['/kisa', 'index', 'Kisat'],
          ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
          ],
          'active_page': { 'id': 'index', 'name': 'Etusivu'}
    }
    return HttpResponse(template.render(context, request))


def detail(request, kilpailu_id):
    template = loader.get_template('jinja2/kisa.html.j2')
    context = {
        'kisa': kilpailu_id,
        'navigation_bar': [
          ['/kisa', 'kisa', 'Kisat'],
          ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
          ],
          'active_page': { 'id': 'kisa', 'name': 'Kisa'}
    }
    return HttpResponse(template.render(context, request))


def lisaa_kisaaja(request):

    template = loader.get_template('jinja2/lisaa_kisaaja.html.j2')
    if request.method == 'POST':
        uusi_kisaaja = Kisaaja(nimi_etu=request.POST['nimi_etu'], nimi_suku=request.POST['nimi_suku'], ruoka_allergiat=request.POST['allergiat'])
        # uusi_kisaaja['nimi_etu'] = request.POST['nimi_etu']
        # uusi_kisaaja['nimi_suku'] = request.POST['nimi_suku']
        # uusi_kisaaja['ruoka_allergiat'] = request.POST['allergiat']
        uusi_kisaaja.save()
        context = {
            'navigation_bar': [
              ['/kisa', 'kisa', 'Kisat'],
              ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
          ],
          'active_page': { 'id': 'lisaa_kisaaja', 'name': 'Kisaajan nimi'}
        }
        return HttpResponse(template.render(context, request))
    else:
        context = {
            'navigation_bar': [
              ['/kisa', 'kisa', 'Kisat'],
              ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
          ],
          'active_page': { 'id': 'lisaa_kisaaja', 'name': 'Lisää kisaaja'}
        }
        return HttpResponse(template.render(context, request))


def add_lajipisteet(request, lajipisteet_id):
    return HttpResponse('Aseta lajipisteet: {}'.format(lajipisteet_id))


def kisaajat(request, kilpailu_id):
    template = loader.get_template('jinja2/kisaajat.html.j2')
    context = {
        'navigation_bar': [
          ['/kisa', 'kisa', 'Kisat'],
          ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
      ],
      'active_page': { 'id': 'kisaajat', 'name': 'Kisa ' + kilpailu_id + ' > Kisaajat'}
    }
    return HttpResponse(template.render(context, request))


def kaikki_kisaajat(request):
    template = loader.get_template('jinja2/kisaajat.html.j2')
    context = {
        'navigation_bar': [
          ['/kisa', 'kisa', 'Kisat'],
          ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
      ],
      'active_page': { 'id': 'kisaajat', 'name': 'Kaikki kisaajat'}
    }
    return HttpResponse(template.render(context, request))


def kisaaja(request, kilpailu_id, kisaaja_id):
    template = loader.get_template('jinja2/kisaaja.html.j2')
    context = {
        'navigation_bar': [
          ['/kisa', 'kisa', 'Kisat'],
          ['/kisa/kisaajat', 'kisaajat', 'Kisaajat']
      ],
      'kisaaja_id': kisaaja_id,
      'active_page': { 'id': 'kisaaja', 'name': 'Kisa ' + kilpailu_id + ' > Kisaaja ' + kisaaja_id}
    }
    return HttpResponse(template.render(context, request))
