from django.contrib import admin

from type_heroes_or_villains.models import SuperType
from .models import Super

# Register your models here.

admin.site.register(Super)
admin.site.register(SuperType)