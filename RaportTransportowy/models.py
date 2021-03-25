from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description=models.TextField()
    price= models.TextField()

class Waluta(models.Model):
    SYMBOL_WALUTY=models.CharField(max_length=3)
    def __str__(self):
        return self.SYMBOL_WALUTY
    class Meta:
        verbose_name_plural = "Waluty"    


class Fabryka(models.Model):
    NAZWA_FABRYKI=models.CharField(max_length=100)
    def __str__(self):
        return self.NAZWA_FABRYKI
    class Meta:
        verbose_name_plural = "Fabryki"


class Status (models.Model):
    NAZWA_STATUSU=models.CharField(max_length=100)
    def __str__(self):
        return self.NAZWA_STATUSU
    class Meta:
        verbose_name_plural = "Statusy"



class Handlowiec(models.Model):
    NAZWA_HANDLOWCA=models.CharField(max_length=100)
    def __str__ (self):
        return self.NAZWA_HANDLOWCA
    class Meta:
        verbose_name_plural = "Handlowcy"

class Pobrane(models.Model):
    NAZWA_POBRANE=models.CharField(max_length=100)
    def __str__ (self):
        return self.NAZWA_POBRANE

class Spedycja(models.Model):
    NAZWA_SPEDYCJA=models.CharField(max_length=100)
    def __str__ (self):
        return self.NAZWA_SPEDYCJA
    class Meta:
        verbose_name_plural='Spedycje'

class Zamawiajacy(models.Model):
    NAZWA_ZAMAWIAJACEGO=models.CharField(max_length=100)
    def __str__ (self):
        return self.NAZWA_ZAMAWIAJACEGO
    class Meta:
        verbose_name_plural='Zamawiający'
class Calopojazdowe(models.Model):
    NAZWA_CALOPOJAZDOWE=models.CharField(max_length=100)
    def __str__ (self):
        return self.NAZWA_CALOPOJAZDOWE
    class Meta:
        verbose_name_plural='Całopojazdowe?'        

class Transport(models.Model):
    PENDING=models.ForeignKey(Status,models.SET_NULL,blank=True,null=True)
    #NUMER_ZAMOWIENIA=models.CharField(max_length=100,blank=True,null=True)
    ZAMAWIAJACY=models.ForeignKey(Zamawiajacy,on_delete=models.SET_NULL, blank=True,null=True)
    CALOPOJAZDOWE=models.ForeignKey(Calopojazdowe,on_delete=models.SET_NULL, blank=True,null=True)
    #
    # ZAMAWIAJACY=models.CharField(max_length=100,blank=True,null=True)
    #CAŁOPOJAZDOWE=models.BooleanField(default=False)
    ILOSC_PALET=models.DecimalField(max_digits=10,decimal_places=0,null=True,blank=True)
    ILOSC_M2=models.DecimalField(max_digits=10,decimal_places=2 ,blank=True,null=True)
    FABRYKA=models.ForeignKey(Fabryka,on_delete=models.SET_NULL, blank=True,null=True)
    HANDLOWIEC=models.ForeignKey(Handlowiec,on_delete=models.SET_NULL, blank=True,null=True)
    SPEDYCJA=models.ForeignKey(Spedycja,on_delete=models.SET_NULL, blank=True,null=True)
    OPIS=models.TextField(blank=True,null=True)
    WALUTA=models.ForeignKey(Waluta,max_length=3, null=True,on_delete=models.SET_NULL,blank=True)
    STAWKA_WYJSCIOWA=models.DecimalField(max_digits=10,decimal_places=2 ,blank=True,null=True)
    STAWKA_WYNEGOCJOWANA=models.DecimalField(max_digits=10,decimal_places=2 ,blank=True,null=True)
    CIAGNIK=models.CharField(max_length=100,blank=True,null=True)
    NACZEPA=models.CharField(max_length=100,blank=True,null=True)
    ZALADUNEK=models.CharField(max_length=100,blank=True,null=True)
    ROZLADUNEK=models.CharField(max_length=100,blank=True,null=True)
    PLANOWANA_DATA_ZALADUNKU=models.DateField(blank=True,null=True)
    DATA_ZALADUNKU=models.DateField(blank=True,null=True)
    DATA_ROZLADUNKU=models.DateField(blank=True,null=True)
    FS=models.CharField(max_length=100,blank=True,null=True)
    DATA_WYSTAWIENIA_FAKTURY=models.DateField(blank=True,null=True)
    DATA_WYSLANIA_SKANU_FAKTURY=models.DateField(blank=True,null=True)
    #DATA_DOSTARCZENIA_DOKUMENTU_TRANSPORTOWEGO=models.DateField(blank=True,null=True)
    NUMER_LISTU_PRZEWOZOWEGO=models.CharField(max_length=100,blank=True,null=True)
    POBRANE=models.ForeignKey(Pobrane,max_length=3, null=True,on_delete=models.SET_NULL,blank=True)
    
    @property
    def spoko(self):
        return(self.NUMER_ZAMOWIENIA)
    @property
    def NUMER(self):
        return(str(self.id)+'/2021')

    class Meta:
        verbose_name_plural = "!Transporty!"
