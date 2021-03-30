from import_export import resources
from RaportTransportowy.models import Transport

class TransportResource(resources.ModelResource):
    class Meta:
        model=Transport