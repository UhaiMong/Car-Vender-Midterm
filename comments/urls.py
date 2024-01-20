from django.urls import path
from . import views
urlpatterns = [
    path('add_comment/', views.comment, name='comments')
]
