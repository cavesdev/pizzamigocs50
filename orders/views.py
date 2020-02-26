from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Pizza, Sub, Pasta, Salad, DinnerPlatter
from .forms import RegisterForm, AuthenticationForm


# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'subs': Sub.objects.all(),
        'pastas': Pasta.objects.all(),
        'salads': Salad.objects.all(),
        'platters': DinnerPlatter.objects.all()
    }
    return render(request, 'orders/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    form = RegisterForm()
    return render(request, 'orders/register.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return redirect('login')
        return redirect('index')
        
    form = AuthenticationForm()
    return render(request, 'orders/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('index')
