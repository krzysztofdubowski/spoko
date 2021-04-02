from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.conf.locale.pl import formats as pl_formats
# Register your models here.
pl_formats.DATETIME_FORMAT="d M D"

from .models import Transport,Waluta,Fabryka,Handlowiec,Status,Spedycja,Zamawiajacy,Calopojazdowe,Pobrane

admin.site.site_header=" APLIKACJE NETTO"
admin.site.site_title="APLIKACJA NETTO"
admin.site.index_title=""

  

@admin.register(Transport)
class TransportAdmin(ImportExportModelAdmin):
    list_display=('NUMER','STATUS','ZAMAWIAJACY','HANDLOWIEC','SPEDYCJA','CALOPOJAZDOWE','ILOSC_PALET','FABRYKA','OPIS','WALUTA','STAWKA_WYJSCIOWA','STAWKA_WYNEGOCJOWANA')
    list_filter=('STATUS','SPEDYCJA','HANDLOWIEC','FABRYKA','DATA_ZALADUNKU','DATA_ROZLADUNKU')
    





admin.site.register(Waluta)
admin.site.register(Fabryka)
admin.site.register(Handlowiec)
admin.site.register(Status)
admin.site.register(Spedycja)
admin.site.register(Zamawiajacy)
admin.site.register(Calopojazdowe)
