from recipes import views

from django.urls import path

urlpatterns = [
    path('create/', views.create_recipe, name='create-recipes'),
    path('read/', views.read_recipe, name='read-recipes'),
    path('read/single/<int:id>/', views.read_recipe_single, name='read-single-recipe'),
    path('get-id/', views.get_id, name='get-id'),
    path('update/single/<int:id>/', views.update_recipe_single, name='update-single-recipe'),
    path('delete/single/<int:id>/', views.delete_recipe_single, name='delete-single-recipe')
]
