from datetime import time
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from recipes.models import Ingredient, Recipe, Step

@login_required(login_url='/user/login/')
def create_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        description = request.POST.get('description', False)
        time_to_cook = request.POST.get('time_to_cook', False)
        image = request.FILES.get('image', False)
        ig_names = request.POST.getlist('ig_names[]', False)
        ig_value = request.POST.getlist('ig_value[]', False)
        ig_unit = request.POST.getlist('ig_unit[]', False)
        steps_to_cook = request.POST.getlist('sc_steps[]', False)        
        
        recipe = Recipe.objects.create(
            user=request.user,
            name=name,
            description=description,
            time_to_cook=time_to_cook,
            image=image
        )
        
        for x in range(len(ig_names)):
            ingredient, ingredient_created = Ingredient.objects.get_or_create(name=ig_names[x], value=ig_value[x], unit=ig_unit[x])
            recipe.ingredients.add(ingredient)
        
        for i in range(len(steps_to_cook)):
            s, s_created = Step.objects.get_or_create(serial_number=i+1, step_to_cook=steps_to_cook[i])
            recipe.steps.add(s)
        
        recipe.save()      
        
    return render(request, 'recipes/create.html')

def read_recipe(request):
    recipes = Recipe.objects.all()
    

    context = {"recipes": recipes}
    
    return render(request, 'recipes/read.html', context)

def read_recipe_single(request, id):
    recipe = Recipe.objects.get(id=id)
    
    context = {"recipe": recipe}
    
    return render(request, 'recipes/read_single.html', context)

def update_recipe_single(request, id):
    recipe = Recipe.objects.get(id=id)
    
    if not(recipe.user == request.user):
        return redirect('index')
    
    if request.method == 'POST':
        name = request.POST.get('name', False)
        description = request.POST.get('description', False)
        time_to_cook = request.POST.get('time_to_cook', False)
        image = request.FILES.get('image', False)
        ig_names = request.POST.getlist('ig_names[]', False)
        ig_value = request.POST.getlist('ig_value[]', False)
        ig_unit = request.POST.getlist('ig_unit[]', False)
        steps_to_cook = request.POST.getlist('sc_steps[]', False)        
        
        recipe.name = name
        recipe.description = description
        recipe.time_to_cook = time_to_cook
        recipe.image = image
        recipe.save()
        
        recipe.ingredients.clear()
        for x in range(len(ig_names)):
            ingredient, ingredient_created = Ingredient.objects.get_or_create(name=ig_names[x], value=ig_value[x], unit=ig_unit[x])
            recipe.ingredients.add(ingredient)
        
        recipe.steps.clear()
        for i in range(len(steps_to_cook)):
            s, s_created = Step.objects.get_or_create(serial_number=i+1, step_to_cook=steps_to_cook[i])
            recipe.steps.add(s)
        
        recipe.save()      
    
    context = {"recipe": recipe}
    return render(request, 'recipes/update_single.html', context)
    

def delete_recipe_single(request, id):
    recipe = Recipe.objects.get(id=id).delete()
    return redirect("read-recipes")