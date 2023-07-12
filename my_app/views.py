from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *

# Create your views here.


def handler404(request, exception):
    return render(request, 'my_app/404.html')


def home(request):
    return render(request, "my_app/home.html")


def profile(request):
    if request.method == "POST":
        name = request.POST['firstName']
        print(name)
    return render(request, "my_app/profile.html")


class AddUser(CreateView):
    form_class = UserForm
    template_name = 'my_app/reg.html'
    success_url = reverse_lazy('home')




