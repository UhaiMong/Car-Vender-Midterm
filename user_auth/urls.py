from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.userLogin.as_view(), name='login'),
    path('signup/', views.userSignup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.editProfile, name='updateProfile'),
    path('logout/', views.userLogout, name='logout'),
]
