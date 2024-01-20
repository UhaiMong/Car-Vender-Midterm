from django.shortcuts import render

# Create your views here.


def userSignup(request):
    return render(request, 'register.html')


def userLogin(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


# def userLogout(request):
#     return render(request)
