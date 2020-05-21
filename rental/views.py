import decimal

from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Car, CarMark, CarCondition, CarClass, Driver, Order


# cars
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
        'title', 'image', 'price_per_hour_usd', 'description', 'color', 'is_car_available', 'layout', 'car_condition',
        'car_mark', 'car_class'
    ]
    template_name = 'rental/cars/edit/car_form.html'


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = [
        'title', 'image', 'price_per_hour_usd', 'description', 'color', 'car_took_counter', 'is_car_available',
        'layout', 'car_condition', 'car_mark', 'car_class'
    ]
    template_name = 'rental/cars/edit/car_update_form.html'

    def test_func(self):
        return True


# additional mark, condition, class edit views
class CarMarkCreateView(LoginRequiredMixin, CreateView):
    model = CarMark
    fields = ['title']
    template_name = 'rental/cars/edit/car_mark_form.html'

    def form_invalid(self, form):
        return HttpResponse("Data in form is invalid!")


class CarConditionCreateView(LoginRequiredMixin, CreateView):
    model = CarCondition
    fields = ['condition']
    template_name = 'rental/cars/edit/car_condition_form.html'


class CarClassCreateView(LoginRequiredMixin, CreateView):
    model = CarClass
    fields = ['title']
    template_name = 'rental/cars/edit/car_mark_form.html'


# drivers
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


class DriverUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Driver
    fields = ['first_name', 'second_name', 'work_experience', 'price']
    template_name = 'rental/drivers/edit/driver_form.html'

    def test_func(self):
        return True


class DriverDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Driver
    context_object_name = 'driver'
    success_url = '/'
    template_name = 'rental/drivers/edit/driver_confirm_delete.html'

    def test_func(self):
        return True


# order stuff
class OrderCarCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'rental/orders/order_car_form.html'
    fields = ['user', 'car', 'driver', 'start_date', 'end_date']

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['car'] = Car.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        initial['driver'] = Driver.objects.get(first_name='No')
        return initial

    def form_valid(self, form):
        if form.cleaned_data['car'].is_car_available and self.request.user == form.cleaned_data['user']:
            days_td = form.cleaned_data['end_date'] - form.cleaned_data['start_date']
            days = days_td.days if days_td.days >= 1 else 1
            total_time = 24 * days
            form.instance.total_hours = total_time
            form.instance.total_price = (
                decimal.Decimal(total_time * 0.3) * form.instance.car.price_per_hour_usd
                + form.instance.driver.price * decimal.Decimal(total_time * 0.3)
            )
            return super().form_valid(form)
        else:
            return HttpResponse('invalid data')


class OrdersCatalogHistoryListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'rental/orders/orders_catalog.html'
    ordering = '-pk'
    paginate_by = 5


class OrdersCatalogPendingListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'rental/orders/orders_catalog.html'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(is_pending=True)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'rental/orders/order_detail.html'


class OrderCancelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['cancel_description']
    template_name = 'rental/orders/edit/order_cancel.html'

    def test_func(self):
        order = Order.objects.get(pk=self.kwargs['pk'])
        order.is_pending = False
        order.is_canceled = True
        order.save()
        return True


def approve_customer_order(request, pk: int):
    order = Order.objects.get(pk=pk)
    order.is_pending = False
    order.is_approved = True
    order.save()
    return redirect('orders-list-all')


def home(request):
    return render(request, 'rental/home.html')


def about(request):
    return render(request, 'rental/about.html')
