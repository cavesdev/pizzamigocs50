from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Sub, Pasta, Salad, DinnerPlatter


# Create your views here.
def index(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'subs': Sub.objects.all(),
        'pastas': Pasta.objects.all(),
        'salads': Salad.objects.all(),
        'platters': DinnerPlatter.objects.all()
    }
    return render(request, 'orders/index.html', context)
