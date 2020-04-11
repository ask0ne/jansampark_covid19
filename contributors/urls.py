from django.urls import path, include
from . import views


app_name = "contributors"

urlpatterns = [
    #Home page
    path('', views.index, name="index"),

    #Register
    path("register/", views.register, name="register"),

]