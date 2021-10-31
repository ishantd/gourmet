from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from accounts.models import UserProfile

class Ingredient(models.Model):
    name = models.CharField(max_length=200, null=True)
    value = models.IntegerField(null=True)
    unit = models.CharField(max_length=200, null=True)

class Step(models.Model):
    serial_number = models.IntegerField(default=1)
    step_to_cook = models.TextField(null=True)

class Recipe(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='recipe')
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.ManyToManyField(Step)
    time_to_cook = models.IntegerField(default=0)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

