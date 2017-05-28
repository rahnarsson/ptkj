from django.db import models
from django import forms
from django.contrib.auth.models import UserManager


# Create your models here.

class Kisaaja(models.Model):
    nimi_etu = models.CharField(max_length=30)
    nimi_suku = models.CharField(max_length=30)
    email = models.CharField(max_length=150, default='')
    ruoka_allergiat = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{} {}'.format(self.nimi_etu, self.nimi_suku)


class Laji(models.Model):
    nimi = models.CharField(max_length=50)

    def __str__(self):
        return self.nimi


class Kilpailu(models.Model):
    nimi = models.CharField(max_length=40)
    vuosi = models.IntegerField(default=0)
    kisaaja = models.ManyToManyField(Kisaaja)
    laji = models.ManyToManyField(Laji)

    def __str__(self):
        return self.nimi


class AikaLaji (models.Model):
    aika = models.DurationField(default=0)
    nimi = models.OneToOneField(Laji)


class Pistelaji(models.Model):
    pisteet = models.IntegerField(default=0)
    nimi = models.OneToOneField(Laji)


class LajiKierros (models.Model):
    laji = models.ForeignKey(Laji)
    kierros_numero = models.IntegerField(default=0)


class LajiPisteet(models.Model):
    laji = models.ForeignKey(Laji)
    kisaaja = models.ForeignKey(Kisaaja)
    pisteet = models.IntegerField(default=0)
    kilpailu = models.ForeignKey(Kilpailu)

    def __str__(self):
        return 'Kilpailu: {} Laji: {} Kisaaja: {} Pisteet: {}'.format(self.kilpailu, self.laji, self.kisaaja, self.pisteet)


class KisaIlmo(models.Model):
    kisaaja = models.ForeignKey(Kisaaja)
    kilpailu = models.ForeignKey(Kilpailu)


class TulosLista(models.Model):
    lajipisteet = models.ForeignKey(LajiPisteet)
    kilpailu = models.ForeignKey(Kilpailu)
    kilpailija = models.ForeignKey(Kisaaja)
    pisteet = models.IntegerField(default=0)

    def __str__(self):
        return 'Kilpailun {} tuloslista'.format(kilpailu)

    def count_points():
        # Count points per kilpailu
        pass

    def sort_by_kilpailu():
        # Sort points by kilpailu
        pass
