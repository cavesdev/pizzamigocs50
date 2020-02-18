from django.contrib import admin
from .models import Pizza, Ingredient, Sub, Pasta, Salad, DinnerPlatter


for model in [Pizza, Ingredient, Sub, Pasta, Salad, DinnerPlatter]:
    admin.site.register(model)
