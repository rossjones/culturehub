from django.contrib import admin
from culturehub.places.models import Place,Restaurant

class PlaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Place, PlaceAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', "address", 'rating', "lat", "long"]

admin.site.register(Restaurant, RestaurantAdmin)