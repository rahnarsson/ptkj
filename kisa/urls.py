from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /kisa/5/
    url(r'^(?P<kilpailu_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /kisa/5/vote/
    url(r'^(?P<lajipisteet_id>[0-9]+)/add_lajipisteet/$', views.add_lajipisteet, name='add_lajipisteet'),
]
