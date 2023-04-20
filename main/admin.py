from django.contrib import admin
from main.models import Country

class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)
