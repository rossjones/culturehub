from django.contrib import admin
from culturehub.events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', "category_names"]

    def category_names(self, obj):
        print obj
        return ','.join([c.title for c in obj.categories.all()])

admin.site.register(Event, EventAdmin)