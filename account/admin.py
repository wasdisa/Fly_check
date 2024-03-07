from django.contrib import admin
from .models import UAVS,Brands,Smodel,Ammo,Rent

# Register your models here.

admin.site.register(UAVS)
admin.site.register(Brands)
admin.site.register(Smodel)
admin.site.register(Ammo)
admin.site.register(Rent)