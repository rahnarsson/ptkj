from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /kisa/5/
    url(r'^(?P<kilpailu_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /kisa/5/vote/
    url(r'^(?P<lajipisteet_id>[0-9]+)/add_lajipisteet/$', views.add_lajipisteet, name='add_lajipisteet'),

    # kaikki järjestelmästä löytyvät kisaajat, voi olla eri kisoihin osallistuneita
    url(r'^kisaajat/$', views.kaikki_kisaajat, name='kaikki_kisaajat'),
    # yksittäisen kisan osallistujat
    url(r'^(?P<kilpailu_id>[0-9]+)/osallistujat/$', views.kisaajat, name='kisaajat'),
    # yksittäisen kisaajan tiedot
    url(r'^kisaaja/(?P<kisaaja_id>[0-9]+)/$', views.kisaaja, name='kisaaja'),
    # lisää kisaaja - modaali
    url(r'^lisaa_kisaaja', views.lisaa_kisaaja, name='lisaa_kisaaja'),
    # osallistujan tiedot -modaali
    url(r'^kisaajainfo/(?P<kisaaja_id>[0-9]+)/$', views.kisaajainfo, name='kisaajainfo'),

    # kaikki järjestelmästä löytyvät lajit, voi olla eri kisoissa käytettyjä
    url(r'^lajit/$', views.lajit, name='lajit'),
    url(r'^lajit/lajityyppiinfo/$', views.lajityyppiinfo, name='lajityyppiinfo'),

    # ilmoittautumislomake
    url(r'^ilmoittaudu/$', views.ilmoittaudu, name='ilmoittaudu')
]
