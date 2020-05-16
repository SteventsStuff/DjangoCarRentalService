from django.contrib import admin

from .models import Car, CarMark, CarClass, CarCondition, Driver


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'price_per_hour_usd', 'color', 'description', 'car_took_counter', 'is_car_available',
        'when_will_be_available', 'last_took_date', 'layout', 'car_condition', 'car_mark', 'car_class',
    )
    list_display_links = ('title',)
    list_filter = ('price_per_hour_usd', 'is_car_available', 'car_condition', 'car_mark', 'car_class')
    search_fields = ('title', 'price_per_hour_usd', 'color',)


class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class CarClassAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class CarConditionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'condition',)
    list_display_links = ('condition',)
    list_filter = ('condition',)
    search_fields = ('condition',)


class DriverAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'second_name', 'work_experience', 'price')
    list_display_links = ('first_name', 'second_name')
    list_filter = ('work_experience', 'price')
    search_fields = ('first_name', 'second_name', 'work_experience', 'price')


admin.site.register(Car, CarAdmin)
admin.site.register(CarMark, CarMarkAdmin)
admin.site.register(CarClass, CarClassAdmin)
admin.site.register(CarCondition, CarConditionAdmin)
admin.site.register(Driver, DriverAdmin)
