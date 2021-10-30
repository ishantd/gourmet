from recipes import views

from django.urls import path

urlpatterns = [
    path('create/', views.create_recipe, name='create-recipes'),
    path('read/', views.read_recipe, name='read-recipes')
]
