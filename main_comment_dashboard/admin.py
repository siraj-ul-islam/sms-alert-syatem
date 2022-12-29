from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(unit_details)
admin.site.register(unit_address_details)

@admin.register(unit_comment_details)
class AddNewVehicleInformation(admin.ModelAdmin):
    list_display = ['unit_address_details_id', 'problem', 'vehicle_no','driver_name']

