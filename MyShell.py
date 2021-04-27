import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django  
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

toppings = Topping.objects.all()
