from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.


from .models import Transport,Waluta,Fabryka,Handlowiec,Status,Spedycja,Zamawiajacy,Calopojazdowe,Pobrane

admin.site.site_header=" APLIKACJE NETTO"
admin.site.site_title="APLIKACJA NETTO"
admin.site.index_title=""

#class Filter(admin.ModelAdmin):
    #list_display=("NUMER_ZAMOWIENIA","SPEDYCJA","FABRYKA","spoko)
    #list_filter=("SPEDYCJA")

@admin.register(Transport)
class TransportAdmin(ImportExportModelAdmin):
    list_display=('NUMER','PENDING','ZAMAWIAJACY','SPEDYCJA','FABRYKA','HANDLOWIEC','OPIS','ILOSC_PALET','CALOPOJAZDOWE')
    list_filter=('PENDING','SPEDYCJA','HANDLOWIEC','FABRYKA','DATA_ZALADUNKU')
    #list_display=[field.name for field in Transport._meta.get_fields()]




#admin.site.register(Transport)
admin.site.register(Waluta)
admin.site.register(Fabryka)
admin.site.register(Handlowiec)
admin.site.register(Status)
admin.site.register(Spedycja)
admin.site.register(Zamawiajacy)
admin.site.register(Calopojazdowe)
admin.site.register(Pobrane)