from django.contrib import admin
from .models import Instance, Device, Spare
# Register your models here.


class InstanceAdmin(admin.ModelAdmin):
    list_display = ('code_text','system_ref','location')
    list_filter = ('code_text','system_ref__name_text','location')


class SpareInline(admin.StackedInline):
    model = Spare
    extra = 1
    fk_name = 'device_ref'

class DeviceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Device Identification', {'fields': ['system_ref', 'location', 'ref', 'index_instance', 'code_text']}),
        ('Date information', {'fields': ['reception_date','install_date']}),
    ]
    inlines = [SpareInline]
    search_fields = ['code_text']

#admin.site.register(Instance)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Spare)
