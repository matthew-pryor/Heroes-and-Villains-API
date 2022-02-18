from django.contrib import admin

from type_heroes_or_villains.models import Super_type
from .models import Super

# Register your models here.

admin.site.register(Super)
admin.site.register(Super_type)