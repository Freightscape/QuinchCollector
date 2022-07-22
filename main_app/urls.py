from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('drinks/', views.drinks_index, name='index'),
  path('drinks/<int:drink_id>/', views.drinks_detail, name='detail'),
  path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
  path('drinks/<int:pk>/update/', views.DrinkUpdate.as_view(), name='drinks_update'),
  path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drinks_delete'),

  path('drinks/<int:drink_id>/add_nutritional/', views.add_nutritional, name='add_nutritional'),
  path('flavors/', views.FlavorList.as_view(), name='flavors_index'),
  path('flavors/<int:pk>/', views.FlavorDetail.as_view(), name='flavors_detail'),
  path('flavors/create/', views.FlavorCreate.as_view(), name='flavors_create'),
  path('flavors/<int:pk>/update/', views.FlavorUpdate.as_view(), name='flavors_update'),
  path('flavors/<int:pk>/delete/', views.FlavorDelete.as_view(), name='flavors_delete'),
  path('drinks/<int:drink_id>/assoc_flavor/<int:flavor_id>/', views.assoc_flavor, name='assoc_flavor'),

]