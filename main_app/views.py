from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Drink, Flavor
from .forms import NutritionalForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

# def drinks_index(request):
#   return render(request, 'drinks/index.html', { 'drinks': drinks }) 
def drinks_index(request):
  drinks = Drink.objects.all()
  return render(request, 'drinks/index.html', { 'drinks': drinks })

def drinks_detail(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  id_list = drink.flavors.all().values_list('id')
  flavors_drink_doesnt_have = Flavor.objects.exclude(id__in=id_list)
  nutritional_form = NutritionalForm()
  return render(request, 'drinks/detail.html', {
    'drink': drink,
    'nutritional_form': nutritional_form,
    'flavors': flavors_drink_doesnt_have 
  })

# Create your views here.
# from django.http import HttpResponse
# class Drink:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, kind, description, price):
#     self.name = name
#     self.kind = kind
#     self.description = description
#     self.price = price

# drinks = [
#   Drink('Pepsi', 'Soda', 'Poplular Pop Drink', 2.79),
#   Drink('Water', 'H20', 'Commercialized Bottled/Drinking Water', 1.79),
#   Drink('Gatorade', 'Sports Drink', 'High Fructose & Eloctrolyte Sports Drink', 2.35)
# ]
class DrinkCreate(CreateView):
  model = Drink
  fields = ['name', 'kind', 'description', 'price']
  #success_url = '/drinks/'

class DrinkUpdate(UpdateView):
  model = Drink
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['kind', 'description', 'price']

class DrinkDelete(DeleteView):
  model = Drink
  success_url = '/drinks/'

def add_nutritional(request, drink_id):
  # create a ModelForm instance using the data in the posted form
  form = NutritionalForm(request.POST)
  # validate the data
  if form.is_valid():
    new_nutritional = form.save(commit=False)
    new_nutritional.drink_id = drink_id
    new_nutritional.save()
  return redirect('detail', drink_id=drink_id)

class FlavorList(ListView):
  model = Flavor

class FlavorDetail(DetailView):
  model = Flavor

class FlavorCreate(CreateView):
  model = Flavor
  fields = '__all__'

class FlavorUpdate(UpdateView):
  model = Flavor
  fields = ['name', 'color']

class FlavorDelete(DeleteView):
  model = Flavor
  success_url = '/flavors/'

def assoc_flavor(request, drink_id, flavor_id):
  Drink.objects.get(id=drink_id).flavors.add(flavor_id)
  return redirect('detail', drink_id=drink_id)