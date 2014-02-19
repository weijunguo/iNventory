from django.contrib import admin
from inventory_tracker.models import Vehicle, SalesPerson

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vin', 'stock', 'description', 'configuration', 'miles')
    search_fields = ['status', 'inventory_type', 'year', 'model', 'brand', 
                     'vin', 'serial', 'stock', 'exterior', 'interior',
                     'transmission', 'options', 'in_date']
    list_filter = ['inventory_type', 'brand', 'model', 'exterior', 'interior',
                   'miles', 'retail', 'in_date']
    


admin.site.register(Vehicle, VehicleAdmin)


