from django.contrib import admin
from wax.models import Wax, Dispensary
# Register your models here.

class WaxAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'pricepergram', 'dispensary', 'type', 'solvent', 'id')
        search_fields = ['name']

class DispensaryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'city', 'address', 'phone', 'website', 'email', 'id')

admin.site.register(Wax, WaxAdmin)
admin.site.register(Dispensary, DispensaryAdmin)
