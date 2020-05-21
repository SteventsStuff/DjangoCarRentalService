from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# todo: use aggregation for index page like: we have N cars, M sutisfied customers, etc
class Car(models.Model):
    title = models.CharField(null=True, blank=False, max_length=100, verbose_name='Title')
    image = models.ImageField(default='car_default.jpg', upload_to='car_pics', verbose_name='Car image')
    price_per_hour_usd = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=2, verbose_name='Price per hours USD'
    )  # todo: add validator
    color = models.CharField(max_length=20, null=True, blank=True, verbose_name='Color')
    description = models.TextField(null=True, blank=True, max_length=400, verbose_name='Description')
    car_took_counter = models.IntegerField(default=0,  verbose_name='Car was taken times')  # todo: add validator
    is_car_available = models.BooleanField(default=False, verbose_name='Is car available')
    when_will_be_available = models.DateTimeField(default=timezone.now, verbose_name='When car will be available')
    last_took_date = models.DateTimeField(default=timezone.now, verbose_name='Last took date')
    layout = models.CharField(max_length=100, null=True, blank=True, verbose_name='Layout')
    car_condition = models.ForeignKey(
        to='CarCondition', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Car condition'
    )
    car_mark = models.ForeignKey(
        to='CarMark', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Car mark'
    )
    car_class = models.ForeignKey(
        to='CarClass', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Car class'
    )

    def __str__(self):
        return f'{self.pk}, {self.title}'

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})


class CarMark(models.Model):
    title = models.CharField(null=True, blank=False, max_length=100, verbose_name='Title')

    def __str__(self):
        return f'{self.title}'

    @staticmethod
    def get_absolute_url():
        return reverse('rental-home')


class CarClass(models.Model):
    title = models.CharField(null=True, blank=False, max_length=100, verbose_name='Title')

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('rental-home')


class CarCondition(models.Model):
    condition = models.CharField(null=True, blank=False, max_length=100, verbose_name='Condition')

    def __str__(self):
        return self.condition

    @staticmethod
    def get_absolute_url():
        return reverse('rental-home')


class Driver(models.Model):
    first_name = models.CharField(null=True, blank=False, max_length=100, verbose_name='First name')
    second_name = models.CharField(null=True, blank=False, max_length=100, verbose_name='Last name')
    work_experience = models.FloatField(null=False, blank=False, verbose_name='Work Experience')  # todo: add validator
    price = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=2, default=1.0, verbose_name='Price'
    )  # todo: add validator

    def __str__(self):
        return f'{self.second_name}, {self.first_name}, {self.work_experience}, {self.price}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    total_price = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=2, default=0.0, verbose_name='Total Price'
    )
    total_hours = models.IntegerField(default=0, verbose_name='Total hours')
    is_approved = models.BooleanField(null=False, blank=False, default=False, verbose_name='Is Approved')
    is_pending = models.BooleanField(null=False, blank=False, default=True, verbose_name='Is Pending')
    is_canceled = models.BooleanField(null=False, blank=False, default=False, verbose_name='Is Canceled')
    cancel_description = models.TextField(
        null=False, blank=False, default='Reason of cancellation:', max_length=500, verbose_name='Cancel description'
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def get_absolute_url(self):
        return reverse('profile-orders', kwargs={'pk': self.user.id})

