from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):  # HttpRequest
# return HttpResponse("Страница приложения main.")
from django.urls import reverse_lazy
from django.views.generic import CreateView


def categories(request, catid):  # HttpRequest
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def Home(request):
    return render(request, 'Home.html', locals())


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
