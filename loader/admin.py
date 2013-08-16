from django.contrib import admin
from loader.models import StateEquiv, CountyEquiv, CountyArchive, StateArchive, NationalArchive

admin.site.register(StateEquiv)
admin.site.register(CountyEquiv)
admin.site.register(CountyArchive)
admin.site.register(StateArchive)
admin.site.register(NationalArchive)
