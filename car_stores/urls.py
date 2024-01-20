from django.urls import path
from . import views
urlpatterns = [
    path('add_car/', views.add_car, name='add_cars'),
    path('details/<int:id>/', views.CarDetailView.as_view(), name='details'),
    path('purchase-car/<int:id>/', views.purchaseCar, name='purchaseCar'),
]
