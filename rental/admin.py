from django.contrib import admin

from .models import Car, CarMark, CarClass, CarCondition, Driver


admin.site.register(Car)
admin.site.register(CarMark)
admin.site.register(CarClass)
admin.site.register(CarCondition)
admin.site.register(Driver)
