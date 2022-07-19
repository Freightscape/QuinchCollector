from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
class Drink:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, kind, description, price):
    self.name = name
    self.kind = kind
    self.description = description
    self.price = price

drinks = [
  Drink('Pepsi', 'Soda', 'Poplular Pop Drink', 2.79),
  Drink('Water', 'H20', 'Commercialized Bottled/Drinking Water', 1.79),
  Drink('Gatorade', 'Sports Drink', 'High Fructose & Eloctrolyte Sports Drink', 2.35)
]


def home(request):
    return HttpResponse('<h1>Welcome to the Quinch Collector</h1>')

def about(request):
    return render(request, 'about.html') 

def drinks_index(request):
  return render(request, 'drinks/index.html', { 'drinks': drinks }) 