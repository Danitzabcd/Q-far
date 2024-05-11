from django.urls import path

from .views import home,index,login

urlpatterns = [
    path("index", index, name="index"),
    path('home', home, name='home'),
     path('login', login, name='login'),
]