from django.contrib import admin
from .models import *


admin.site.register(Garage)
admin.site.register(Recommendations)
admin.site.register(Comments)

class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'generation', 'body_type', 'fuel_type', 'motor', 'gearbox', 'wheel_drive', 'about', 'car_photo')
admin.site.register(Cars, CarsAdmin)

class CarModelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name')
admin.site.register(CarModels, CarModelsAdmin)

class GenerationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'gen', 'drom_gen')
admin.site.register(Generations, GenerationsAdmin)

class BodyTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'body')
admin.site.register(BodyTypes, BodyTypesAdmin)

class FuelTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fuel')
admin.site.register(FuelTypes, FuelTypesAdmin)

class MotorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gen', 'engine')
admin.site.register(Motors, MotorsAdmin)

class GearboxesAdmin(admin.ModelAdmin):
    list_display = ('id', 'gear')
admin.site.register(Gearboxes, GearboxesAdmin)

class WheelDrivesAdmin(admin.ModelAdmin):
    list_display = ('id', 'wd')
admin.site.register(WheelDrives, WheelDrivesAdmin)
