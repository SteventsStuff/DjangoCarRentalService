from django.contrib import admin

from .models import Car, CarMark, CarClass, CarCondition, Driver, Order


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'price_per_hour_usd', 'color', 'description', 'is_car_available', 'layout', 'car_condition',
        'car_mark', 'car_class',
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


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'car', 'driver', 'total_price', 'total_hours', 'is_approved',  'is_pending', 'is_canceled',
        'start_date', 'end_date'
    )
    list_display_links = ('user', 'car', 'driver')
    list_filter = ('car', 'driver')
    search_fields = ('user', 'car', 'driver', 'start_date', 'end_date')


admin.site.register(Car, CarAdmin)
admin.site.register(CarMark, CarMarkAdmin)
admin.site.register(CarClass, CarClassAdmin)
admin.site.register(CarCondition, CarConditionAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Order, OrderAdmin)
