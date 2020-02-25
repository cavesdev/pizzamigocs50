from django.db import models


class Pizza(models.Model):
    PIZZA_TYPE = [
        ('R', 'Regular'),
        ('S', 'Sicilian')
    ]

    TOPPING_COUNT = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=1, choices=PIZZA_TYPE)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    topping_count = models.PositiveSmallIntegerField(choices=TOPPING_COUNT, default=0)

    def __str__(self):
        return f'{"Regular" if self.type == "R" else "Sicilian"} {self.name} Pizza'


class Ingredient(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Sub(models.Model):
    name = models.CharField(max_length=25)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name} Sub'


class Pasta(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class DinnerPlatter(models.Model):
    name = models.CharField(max_length=25)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name} Platter'


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza, blank=True)
    pizza_toppings = models.ManyToManyField(Ingredient, blank=True)
    subs = models.ManyToManyField(Sub, blank=True)
    pastas = models.ManyToManyField(Pasta, blank=True)
    salads = models.ManyToManyField(Salad, blank=True)
    platters = models.ManyToManyField(DinnerPlatter, blank=True)
    # extras = models.ManyToManyField(Ingredient, blank=True)

    total_price = models.DecimalField(max_digits=5, decimal_places=2)
