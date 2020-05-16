from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Car, CarMark, Driver


class CarRentalListView(ListView):
    model = Car
    template_name = 'rental/cars/cars-catalog.html'
    context_object_name = 'cars'
    ordering = ['price_per_hour_usd']
    paginate_by = 5


class CarMarkListView(ListView):
    model = Car
    template_name = 'rental/cars/filters/car_mark.html'
    context_object_name = 'cars'
    ordering = ['title']
    paginate_by = 5

    def get_queryset(self):
        mark_object = get_object_or_404(CarMark, title=self.kwargs.get('mark_title'))
        return Car.objects.filter(car_mark__title=mark_object.title)


class CarDetailView(DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'rental/cars/filters/car_detail.html'


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    context_object_name = 'car'
    success_url = '/'
    template_name = 'rental/cars/edit/car_confirm_delete.html'

    def test_func(self):
        return True


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = [
        'title', 'image', 'price_per_hour_usd', 'description', 'color', 'car_took_counter', 'is_car_available',
        'layout', 'car_condition', 'car_mark', 'car_class'
    ]
    template_name = 'rental/cars/edit/car_form.html'

    # def form_valid(self, form):
    #     # form.instance.
    #     # return super().form_valid(form)
    #     pass


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = [
        'title', 'image', 'price_per_hour_usd', 'description', 'color', 'car_took_counter', 'is_car_available',
        'layout', 'car_condition', 'car_mark', 'car_class'
    ]
    template_name = 'rental/cars/edit/car_form.html'

    def test_func(self):
        return True
        # car = self.get_object()
        # if self.request.user == car.author:
        #     return True
        # return False

    # def form_valid(self, form):
    #     # form.instance.
    #     # return super().form_valid(form)
    #     pass


class DriversListView(ListView):
    model = Driver
    template_name = 'rental/drivers/drivers-catalog.html'
    context_object_name = 'drivers'
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    template_name = 'rental/drivers/drivers-detail.html'
    context_object_name = 'driver'


class DriverCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    fields = ['first_name', 'second_name', 'work_experience', 'price']
    template_name = 'rental/cars/edit/car_form.html'

    # def form_valid(self, form):
    #     # form.instance.
    #     # return super().form_valid(form)
    #     pass


class DriverUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Driver
    fields = ['first_name', 'second_name', 'work_experience', 'price']
    template_name = 'rental/drivers/edit/driver_form.html'

    def test_func(self):
        return True
        # car = self.get_object()
        # if self.request.user == car.author:
        #     return True
        # return False

    # def form_valid(self, form):
    #     # form.instance.
    #     # return super().form_valid(form)
    #     pass


class DriverDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Driver
    context_object_name = 'driver'
    success_url = '/'
    template_name = 'rental/drivers/edit/driver_confirm_delete.html'

    def test_func(self):
        return True


def home(request):
    return render(request, 'rental/home.html')


def about(request):
    return render(request, 'rental/about.html')
