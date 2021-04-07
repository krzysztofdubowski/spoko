from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.conf.locale.pl import formats as pl_formats
from RaportTransportowy.resources import TransportResource
from django.contrib import messages
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.utils.translation import ngettext
from django.contrib.admin import DateFieldListFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.
pl_formats.DATETIME_FORMAT="d M D"

from .models import Transport,Waluta,Fabryka,Handlowiec,Status,Spedycja,Zamawiajacy,Calopojazdowe,Pobrane

admin.site.site_header=" APLIKACJE NETTO V 1.0"
admin.site.site_title="APLIKACJA NETTO"
admin.site.index_title=""

  

@admin.register(Transport)
class TransportAdmin(ImportExportModelAdmin):
    list_display=('NUMER','STATUS','ZAMAWIAJACY','HANDLOWIEC','SPEDYCJA','CALOPOJAZDOWE','ILOSC_PALET','FABRYKA','OPIS','WALUTA','STAWKA_WYJSCIOWA','STAWKA_WYNEGOCJOWANA')
    list_filter=(
        ('STATUS',RelatedDropdownFilter),
        ('SPEDYCJA',RelatedDropdownFilter),
        ('HANDLOWIEC',RelatedDropdownFilter),
        ('FABRYKA',RelatedDropdownFilter),
        ('DATA_ZALADUNKU',DateRangeFilter),
        ('DATA_ROZLADUNKU',DateRangeFilter),
        ('ZAMAWIAJACY',RelatedDropdownFilter)
        )
    resource_class=TransportResource
    





admin.site.register(Waluta)
admin.site.register(Fabryka)
admin.site.register(Handlowiec)
admin.site.register(Status)
admin.site.register(Spedycja)
admin.site.register(Zamawiajacy)
admin.site.register(Calopojazdowe)
