from django.shortcuts import render
from car_stores.models import Car, Brand


def home(request, brand_name=None):
    cars = Car.objects.all()
    static_text = "Welcome to our car store! Explore our amazing collection of cars."
    image = "car_stores/static/ferrari_top.jpg"
    if brand_name is not None:
        brand = Brand.objects.get(name=brand_name)
        cars = Car.objects.filter(brand=brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands, 'text': static_text, 'img': image})
