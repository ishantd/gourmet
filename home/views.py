from django.shortcuts import render
from recipes.models import Recipe

def index(request):
    recipes = Recipe.objects.all()[:4]
    context = {"recipes": recipes}
    return render(request, 'home/index.html', context)