from django.contrib import admin

# Register your models here.


from .models import Transport,Waluta,Fabryka,Handlowiec,Status,Spedycja

admin.site.site_header="NETTO"
admin.site.site_title="APLIKACJA NETTO"
admin.site.index_title=""

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    #list_display=('SPEDYCJA','FABRYKA')
    list_display=[field.name for field in Transport._meta.get_fields()]

#admin.site.register(Transport)
admin.site.register(Waluta)
admin.site.register(Fabryka)
admin.site.register(Handlowiec)
admin.site.register(Status)
admin.site.register(Spedycja)