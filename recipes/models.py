from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200, null=True)
    value = models.IntegerField(null=True)
    unit = models.CharField(max_length=200, null=True)

class Step(models.Model):
    serial_number = models.IntegerField(default=1)
    step_to_cook = models.TextField(null=True)

class Recipe(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.ManyToManyField(Step)
    time_to_cook = models.IntegerField(default=0)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
