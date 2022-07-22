from django.forms import ModelForm
from .models import Nutritional

class NutritionalForm(ModelForm):
  class Meta:
    model = Nutritional
    fields = ['date', 'macro']
