# Generated by Django 3.2.8 on 2021-11-01 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='value',
            field=models.CharField(max_length=200, null=True),
        ),
    ]