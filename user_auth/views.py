from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from car_stores.models import Purchase

# Create your views here.


def userSignup(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')

    else:
        register_form = forms.RegistrationForm()
    return render(request, 'signup.html', {'form': register_form, 'type': 'Signup'})


class userLogin(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('homepage')

    def get_success_url(self):
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged In FAiled!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def profile(request):
    if request.user.is_authenticated:
        user_purchases = Purchase.objects.filter(buyer=request.user)
        user = request.user
        data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return render(request, 'profile.html', {'data': data, 'user_purchases': user_purchases})
    else:
        return redirect('login')


def editProfile(request):
    if request.method == 'POST':
        formUpdate = forms.ChangeUserForm(
            request.POST, instance=request.user)
        if formUpdate.is_valid():
            formUpdate.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')

    else:
        formUpdate = forms.ChangeUserForm(instance=request.user)
    return render(request, 'updateProfile.html', {'form': formUpdate})


def userLogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')
