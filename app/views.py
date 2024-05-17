from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from decimal import Decimal


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})


# def add_car(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('car_list')
#     else:
#         form = CarForm()
#     return render(request, 'cars/car_add.html', {'form': form})

def add_car(request):
    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        year = int(request.POST['year'])
        color = request.POST['color']
        mileage = float(request.POST['mileage'])
        price = Decimal(request.POST['price'])
        fuel_type = request.POST['fuel_type']
        transmission = request.POST['transmission']

        Car.objects.create(
            make=make,
            model=model,
            year=year,
            color=color,
            mileage=mileage,
            price=price,
            fuel_type=fuel_type,
            transmission=transmission
        )
        return redirect('car_list')
    else:
        return render(request, 'cars/add_car.html')
