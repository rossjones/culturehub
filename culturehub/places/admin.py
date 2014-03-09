from django.contrib import admin
from culturehub.places.models import Place

class PlaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Place, PlaceAdmin)