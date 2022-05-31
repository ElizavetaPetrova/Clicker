from django.contrib import admin

# Register your models here.
from .models import Core, Boost

admin.site.register(Core)
admin.site.register(Boost)