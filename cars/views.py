
from django.http import HttpResponse

from cars.forms import CarForm
from cars.models import Car
from django.shortcuts import render, redirect


def index(request):
    cars = Car.objects.all()
    return render(request, "index.html", {"cars": cars})


def add_car(request):
    if not request.user.is_authenticated:
        return HttpResponse("You aren't authenticated!")

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            Car.objects.create(user=request.user, **form.cleaned_data)
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})
