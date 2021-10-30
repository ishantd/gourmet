from django.shortcuts import render


def create_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        description = request.POST.get('description', False)
        time_to_cook = request.POST.get('time_to_cook', False)
        image = request.FILES.get('image', False)
        igs = request.POST.getlist('ig_names[]', False)
        print(name, description, time_to_cook, image, igs)
        
    return render(request, 'recipes/create.html')
