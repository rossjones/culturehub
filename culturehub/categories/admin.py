from django.contrib import admin
from culturehub.categories.models import Category

def make_interesting(modeladmin, request, queryset):
    queryset.update(interesting=True)
make_interesting.short_description = "Mark selected categories as interesting"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'interesting']
    actions = [make_interesting]

admin.site.register(Category, CategoryAdmin)