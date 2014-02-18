from django.contrib import admin
from inventory_tracker.models import Vehicle, SalesPerson

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vin', 'stock', 'description', 'configuration', 'miles')
    search_fields = ['vin']
    list_filter = ['inventory_type', 'brand', 'model', 'exterior', 'interior']
    

admin.site.register(Vehicle, VehicleAdmin)


