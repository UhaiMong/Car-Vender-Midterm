from . import models
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Purchase, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


def add_car(request):
    if request.method == 'POST':
        car = forms.carAddForm(request.POST)
        if car.is_valid():
            print(car)
            car.save()
            return redirect('homepage')
    else:
        car = forms.carAddForm()

    return render(request, 'car_stores.html', {'car': car})


class CarDetailView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.car = self.object
            new_comment.save()
        return self.render_to_response(self.get_context_data(form=form))


@login_required
def purchaseCar(request, id):
    car = get_object_or_404(Car, pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        purchase = Purchase.objects.create(buyer=request.user, car=car)

        return render(request, 'purchase_success.html', {'car': car, 'purchase': purchase})
    else:
        return render(request, 'purchase_fail.html', {'car': car})
