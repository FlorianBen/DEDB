from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Reference, Manufacturer
# Register your models here.


class ReferenceAdmin(SimpleHistoryAdmin):
    list_display = ('name_text', 'manufacturer', 'ref_manufacturer_text', 'status')
    list_filter = ('manufacturer', 'status', 'tags__name')
    search_fields = ['name_text', 'tags__name']
    fieldsets = [
        ('Reference information', {'fields': [
         'name_text', 'manufacturer','ref_manufacturer_text', 'website_url']}),
        ('Status information', {'fields': ['solution', 'status']}),
        ('Misc', {'fields': ['picture','tags']}),
    ]


class ManufacturerAdmin(SimpleHistoryAdmin):
    list_display = ('name_text', 'type', 'status')
    list_filter = ('name_text', 'type', 'status')
    search_fields = ["name_text"]
    fieldsets = [
        ('Manufacturer information', {'fields': ['name_text', 'type', 'website_url']}),
        ('Status information', {'fields': ['status', 'new_manufacturer']}),
        ('Misc', {'fields': ['logo_file']}),
    ]


admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
