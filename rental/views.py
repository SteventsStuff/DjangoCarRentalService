from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Car, CarMark


class CarRentalListView(ListView):
    model = Car
    template_name = 'rental/catalog.html'
    context_object_name = 'cars'
    ordering = ['price_per_hour_usd']
    paginate_by = 5


class CarMarkListView(ListView):
    model = Car
    template_name = 'rental/car_mark.html'
    context_object_name = 'posts'
    ordering = ['title']
    paginate_by = 5

    def get_queryset(self):
        mark_object = get_object_or_404(CarMark, title=self.kwargs.get('mark_title'))
        print(mark_object.title, 'aaaaaaaaaaaa')
        return Car.objects.filter(car_mark__title=mark_object.title)


class CarDetailView(DetailView):
    model = Car
    context_object_name = 'car'


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    context_object_name = 'car'
    success_url = '/'

    def test_func(self):
        return True


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['title', 'description']

    # def form_valid(self, form):
    #     # form.instance.
    #     # return super().form_valid(form)
    #     pass


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = ['title', 'description']

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


def home(request):
    return render(request, 'rental/home.html')


def about(request):
    context = {
        'title': 'kek'
    }
    return render(request, 'rental/about.html', context)
