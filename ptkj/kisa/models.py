from django.db import models

# Create your models here.
class Kisaaja(models.Model):
    nimi_etu = models.CharField(max_length=30)
    nimi_suku = models.CharField(max_length=30)
    def __str__(self):
        return '{} {}'.format(self.nimi_etu, self.nimi_suku)


class Kilpailu(models.Model):
    nimi = models.CharField(max_length=40)
    vuosi = models.IntegerField(default=0)
    def __str__(self):
        return self.nimi


class Laji(models.Model):
    nimi = models.CharField(max_length=50)
    kilpailu = models.ForeignKey(Kilpailu)
    def __str__(self):
        return self.nimi


class LajiPisteet(models.Model):
    laji = models.ForeignKey(Laji)
    kisaaja = models.ForeignKey(Kisaaja)
    pisteet = models.IntegerField(default=0)
    kilpailu = models.ForeignKey(Kilpailu)
    def __str__(self):
        return 'Kilpailu: {} Laji: {} Kisaaja: {} Pisteet: {}'.format(self.kilpailu, self.laji, self.kisaaja, self.pisteet)
