from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),

]