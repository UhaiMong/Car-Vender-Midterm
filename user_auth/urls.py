from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('signup/', views.userSignup, name='signup'),
    path('profile/', views.profile, name='profile')
]
