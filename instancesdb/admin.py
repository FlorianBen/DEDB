from django.contrib import admin
from .models import Instance, Device, Spare
# Register your models here.

admin.site.register(Instance)
admin.site.register(Device)
admin.site.register(Spare)