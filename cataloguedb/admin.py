from django.contrib import admin
from .models import Reference, Manufacturer
# Register your models here.


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name_text', 'manufacturer', 'ref_manufacturer_text', 'status')
    list_filter = ('manufacturer', 'status', 'tags__name')
    search_fields = ['name_text', 'tags__name']
    fieldsets = [
        ('Reference information', {'fields': [
         'name_text', 'manufacturer','ref_manufacturer_text', 'website_url']}),
        ('Status information', {'fields': ['solution', 'status']}),
        (None, {'fields': ['tags']}),
    ]


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name_text', 'status')
    list_filter = ('name_text', 'status')
    search_fields = ["name_text"]
    fieldsets = [
        ('Manufacturer information', {'fields': ['name_text', 'website_url']}),
        ('Status information', {'fields': ['status', 'new_manufacturer']}),
    ]


admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
