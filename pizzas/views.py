from django.shortcuts import render
from .models import Pizza, Topping
from .forms import CommentForm

# Create your views here.

def index(request):
    ''' The home page for da pizzas. '''
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    toppings = pizza.topping_set.order_by('name')

    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)


def new_comment(request):
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.save()

            return redirect('pizzas:pizza')
    context = {'form':form}
    return render(request, 'pizzas/new_comment.html', context)


