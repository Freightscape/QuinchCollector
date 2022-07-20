from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Drink
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  fields = '__all__'
  success_url = '/drinks/'

class DrinkUpdate(UpdateView):
  model = Drink
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['kind', 'description', 'price']

class DrinkDelete(DeleteView):
  model = Drink
  success_url = '/drinks/'

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
  return render(request, 'drinks/detail.html', { 'drink': drink })