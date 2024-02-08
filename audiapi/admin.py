from django.contrib import admin
from .models import *

admin.site.register(Cars)



admin.site.register(Garage)
admin.site.register(Recommendations)
admin.site.register(Comments)

class GearboxesAdmin(admin.ModelAdmin):
    list_display = ('id', 'gear', 'wd')
admin.site.register(Gearboxes, GearboxesAdmin)

class GenerationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name', 'gen', 'body')
admin.site.register(Generations, GenerationsAdmin)

class MotorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gen', 'fuel', 'engine', 'gear')
admin.site.register(Motors, MotorsAdmin)
