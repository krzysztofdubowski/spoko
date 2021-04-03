from import_export import resources,fields,widgets
from RaportTransportowy.models import Transport,Status
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

class TransportResource(resources.ModelResource):
    
    NUmer=fields.Field(
        column_name='NUMER',
        attribute='NUMER',
        #widget=ForeignKeyWidget(Status,'NAZWA_STATUSU')
    )
    
    Status=fields.Field(
        column_name='STATUS',
        attribute='STATUS',
        #widget=ForeignKeyWidget(Status,'NAZWA_STATUSU')
    )
    
    Zamawiajacy=fields.Field(
        column_name='ZAMAWIAJACY',
        attribute='ZAMAWIAJACY',
        
    )
    
    Calopojazdowe=fields.Field(
        column_name='CALOPOJAZDOWE',
        attribute='CALOPOJAZDOWE',
        
    )

    IloscPalet=fields.Field(
        column_name='ILOSC_PALET',
        attribute='ILOSC_PALET',
        
    )

    IloscM2=fields.Field(
        column_name='ILOSC_M2',
        attribute='ILOSC_M2',
        
    )
    
    Fabryka=fields.Field(
        column_name='FABRYKA',
        attribute='FABRYKA',
        
    )

    Handlowiec=fields.Field(
        column_name='HANDLOWIEC',
        attribute='HANDLOWIEC',
        
    )
    Spedycja=fields.Field(
        column_name='SPEDYCJA',
        attribute='SPEDYCJA',
        
    )

    Opis=fields.Field(
        column_name='OPIS',
        attribute='OPIS',
        
    )

    Waluta=fields.Field(
        column_name='WALUTA',
        attribute='WALUTA',
        
    )
    
    StawkaWyjsciowa=fields.Field(
        column_name='STAWKA_WYJSCIOWA',
        attribute='STAWKA_WYJSCIOWA',
        
    )

    StawkaWynegocjowana=fields.Field(
        column_name='STAWKA_WYNEGOCJOWANA',
        attribute='STAWKA_WYNEGOCJOWANA',
        
    )
    
    Ciagnik=fields.Field(
        column_name='CIAGNIK',
        attribute='CIAGNIK',
        
    )

    Naczepa=fields.Field(
        column_name='NACZEPA',
        attribute='NACZEPA',
        
    )

    Zaladunek=fields.Field(
        column_name='ZALADUNEK',
        attribute='ZALADUNEK',
        
    )
    
    Rozladunek=fields.Field(
        column_name='ROZLADUNEK',
        attribute='ROZLADUNEK',
        
    )

    PlanowanaDataZaladunku=fields.Field(
        column_name='PLANOWANA_DATA_ZALADUNKU',
        attribute='PLANOWANA_DATA_ZALADUNKU',
        
    )

    DataZaladunku=fields.Field(
        column_name='DATA_ZALADUNKU',
        attribute='DATA_ZALADUNKU',
        
    )

    DataRozladunku=fields.Field(
        column_name='DATA_ROZLADUNKU',
        attribute='DATA_ROZLADUNKU',
        
    )

    fs=fields.Field(
        column_name='FS',
        attribute='FS',
        
    )

    DataWystawieniaFaktury=fields.Field(
        column_name='DATA_WYSTAWIENIA_FAKTURY',
        attribute='DATA_WYSTAWIENIA_FAKTURY',
        
    )

    DataWyslaniaSkanuFaktury=fields.Field(
        column_name='DATA_WYSLANIA_SKANU_FAKTURY',
        attribute='DATA_WYSLANIA_SKANU_FAKTURY',
        
    )

    NuerListuPrzewozowego=fields.Field(
        column_name='NUMER_LISTU_PRZEWOZOWEGO',
        attribute='NUMER_LISTU_PRZEWOZOWEGO',
        
    )

    Pobrane=fields.Field(
        column_name='POBRANE',
        attribute='POBRANE',
        
    )
    


    class Meta:
        model=Transport
        fields=('STATUS')
        