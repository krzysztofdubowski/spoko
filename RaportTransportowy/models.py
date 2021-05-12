from django.db import models
from django.contrib.auth.models import User
from import_export import widgets

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
    class Meta:
        verbose_name_plural='Pobrane'    

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
    MIESIACE=(
        ('1.styczen',('1.styczen')),
        ('2.luty',('2.luty')),
        ('3.marzec',('3.marzec')),
        ('4.kwiecień',('4.kwiecień')),
        ('5.maj',('5.maj')),
        ('6.czerwiec',('6.czerwiec')),
        ('7.lipiec',('7.lipiec')),
        ('8.sierpień',('8.sierpirń')),
        ('9.wrzesień',('9.wrzesień')),
        ('10.październik',('10.październik')),
        ('11.listopad',('11.listopad')),
        ('12.grudzień',('12.grudzień')),
    )
    STATUS=models.ForeignKey(Status,models.SET_NULL,blank=True,null=True)
    MIESIAC=models.CharField(max_length=20,choices=MIESIACE,blank=True,null=True)
    ZAMAWIAJACY=models.ForeignKey(Zamawiajacy,on_delete=models.SET_NULL, blank=True,null=True)
    CALOPOJAZDOWE=models.ForeignKey(Calopojazdowe,on_delete=models.SET_NULL, blank=True,null=True)
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
    NUMER_LISTU_PRZEWOZOWEGO=models.CharField(max_length=100,blank=True,null=True)
    POBRANE=models.ForeignKey(Pobrane,max_length=3, null=True,on_delete=models.SET_NULL,blank=True)
    
    NUMER_ZALADUNKOWY=models.TextField(max_length=500,blank=True,null=True)
    NAZWA_KLIENTA=models.TextField(max_length=500,blank=True,null=True)
    NAZWA_HANDLOWCA=models.TextField(max_length=500,blank=True,null=True)
    OPIS_POLACZONYCH=models.TextField(blank=True,null=True)
    
    
    def __unicode__(self):
        return (str(self.id)+'/2021')
    def daj_numer(self):
       return str(self.id)+'/RT'


    
    @property
    def NUMER(self):
        return(str(self.id)+'/RT')
    
    @property
    def STATUS_LACZENIA(self):
        return(str(self.id)+'/RT')

    class Meta:
        verbose_name_plural = "!Transporty!"


