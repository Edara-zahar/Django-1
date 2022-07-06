from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
