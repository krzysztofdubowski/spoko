from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.conf.locale.pl import formats as pl_formats
from RaportTransportowy.resources import TransportResource
from django.contrib import messages
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter,RelatedOnlyFieldListFilter,RelatedFieldListFilter
from django.utils.translation import ngettext
from django.contrib.admin import DateFieldListFilter,SimpleListFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
#from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from import_export import widgets
from django.utils.translation import gettext_lazy as _

# Register your models here.
pl_formats.DATETIME_FORMAT="d M D"

from .models import Transport,Waluta,Fabryka,Handlowiec,Status,Spedycja,Zamawiajacy,Calopojazdowe,Pobrane

admin.site.site_header=" APLIKACJE NETTO V4"
admin.site.site_title="APLIKACJA NETTO"
admin.site.index_title=""

def Polacz(modeladmin, request,queryset):
    wiadomosc=''
    StatusPolaczone=Status.objects.get(NAZWA_STATUSU='POŁĄCZONE')
    StatusZlaczone=Status.objects.get(NAZWA_STATUSU='ZŁĄCZONE/ ZREALIZOWANE')
    StatusCalopojazdowe=Calopojazdowe.objects.get(NAZWA_CALOPOJAZDOWE='Całopojazdowe')
    #Polacz.short_description = "Polacz transporty"
    TransPolaczone=Transport()
    TransPolaczone.OPIS='Zamówienie powstało z połączenia zamówień '
    TransPolaczone.STATUS=StatusZlaczone
    TransPolaczone.CALOPOJAZDOWE=StatusCalopojazdowe
    TransPolaczone.NUMER_ZALADUNKOWY=''
    TransPolaczone.NAZWA_KLIENTA=''
    TransPolaczone.NAZWA_HANDLOWCA=''
    TransPolaczone.save()
    id_zamowienia=str(TransPolaczone.id)
    print('id zamowienia ='+id_zamowienia)
    sumaPalet=0
    sumaM2=0

    for obj in queryset:
        
        sumaPalet=sumaPalet+obj.ILOSC_PALET
        sumaM2=sumaM2+obj.ILOSC_M2

        print(obj.id)
        Klient=obj.ZAMAWIAJACY
        Handlowiec=obj.HANDLOWIEC

        obj.OPIS_POLACZONYCH='Zamówienie połączone do zamówienia:'+id_zamowienia+' '+obj.OPIS
        obj.STATUS=StatusPolaczone
        obj.save()

        TransPolaczone.OPIS=TransPolaczone.OPIS+obj.daj_numer()+' Opis:'+obj.OPIS
        #TransPolaczone.OPIS=TransPolaczone.OPIS+obj.OPIS+'\n'
        TransPolaczone.NUMER_ZALADUNKOWY=str('' if obj.NUMER_ZALADUNKOWY is None else obj.NUMER_ZALADUNKOWY+';')+TransPolaczone.NUMER_ZALADUNKOWY+obj.daj_numer()+';'
        TransPolaczone.NAZWA_KLIENTA=TransPolaczone.NAZWA_KLIENTA+str('' if Klient is None else Klient.NAZWA_ZAMAWIAJACEGO+';')
        TransPolaczone.NAZWA_HANDLOWCA=TransPolaczone.NAZWA_HANDLOWCA+str('' if Handlowiec is None else Handlowiec.NAZWA_HANDLOWCA+';')
        TransPolaczone.ILOSC_PALET=sumaPalet
        TransPolaczone.ILOSC_M2=sumaM2
        
        
        TransPolaczone.save()
        
class FiltrStatusow(SimpleListFilter):
    title="FILTR STATUSÓW"
    parameter_name='Status_transportu'
    def lookups(self,request,model_admin):
        return (
            ('ŁĄCZONE','ŁĄCZONE'),
            ('NIEŁĄCZONE','NIEŁĄCZONE')

        )
    def queryset(self,request,queryset):
        if not self.value():
            return queryset
        if self.value()=='ŁĄCZONE':
            #return queryset
            return queryset.exclude(STATUS=='1')
        if self.value()=='NIEŁĄCZONE':
            return queryset    

        


@admin.register(Transport)
class TransportAdmin(ImportExportModelAdmin):
    list_display=('NUMER','OPIS','STATUS','NUMER_ZALADUNKOWY','NAZWA_KLIENTA','NAZWA_HANDLOWCA','ZAMAWIAJACY','HANDLOWIEC','SPEDYCJA','CALOPOJAZDOWE','ILOSC_PALET','ILOSC_M2','FABRYKA','OPIS','WALUTA','STAWKA_WYJSCIOWA','STAWKA_WYNEGOCJOWANA')
    list_filter=(
        ('MIESIAC',DropdownFilter),
        ('STATUS',RelatedDropdownFilter),
        ('SPEDYCJA',RelatedDropdownFilter),
        ('HANDLOWIEC',RelatedDropdownFilter),
        ('FABRYKA',RelatedDropdownFilter),
        ('DATA_ZALADUNKU',DateRangeFilter),
        ('DATA_ROZLADUNKU',DateRangeFilter),
        ('ZAMAWIAJACY',RelatedDropdownFilter),
        #FiltrStatusow,
        )
    
    list_display_likns=('ZAMAWIAJACY',)
    search_fields=('id','OPIS','NUMER_ZALADUNKOWY','NAZWA_KLIENTA','NAZWA_HANDLOWCA')
    resource_class=TransportResource
    actions = [Polacz]


admin.site.register(Waluta)
admin.site.register(Fabryka)
admin.site.register(Handlowiec)
admin.site.register(Status)
admin.site.register(Spedycja)
admin.site.register(Zamawiajacy)
admin.site.register(Calopojazdowe)
admin.site.register(Pobrane)

