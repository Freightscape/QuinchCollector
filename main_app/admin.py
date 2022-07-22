from django.contrib import admin
from .models import Drink, Nutritional, Flavor
# Register your models here.

admin.site.register(Drink)
admin.site.register(Nutritional)
admin.site.register(Flavor)