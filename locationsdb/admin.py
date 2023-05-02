from django.contrib import admin
from .models import Installation, Office, Level, Unit, Room, Zone, Area
# Register your models here.

#admin.site.register(Location)
#admin.site.register(Building)
admin.site.register(Installation)
admin.site.register(Office)
admin.site.register(Level)
admin.site.register(Area)
admin.site.register(Room)
#admin.site.register(Zone)
admin.site.register(Unit)
