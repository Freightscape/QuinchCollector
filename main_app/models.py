from django.db import models
from django.urls import reverse
from datetime import date

MACROS = (
    ('N', 'No-Sugar'),
    ('L', 'Low-Carbs'),
    ('H', 'High-Protein')
)

class Flavor(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('flavors_detail', kwargs={'pk': self.id})

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    flavors = models.ManyToManyField(Flavor)
   
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})

    def nutrtrients_for_today(self):
        return self.nutritional_set.filter(date=date.today()).count() >= len(MACROS)
    
class Nutritional(models.Model):
  date = models.DateField('Entry Date')
  macro = models.CharField(
    'MACRO Stats',
    max_length=1,
    choices=MACROS,
    default=MACROS[0][0]
  )
  # create a cat_id column in the db
  drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_macro_display()} on {self.date}"

  class Meta:
    ordering = ['-date']  