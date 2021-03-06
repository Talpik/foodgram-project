import csv

from django.core.management.base import BaseCommand, CommandError
from recipes.models import Ingredient, ProductCategory


class Command(BaseCommand):
    help = 'Load ingredients in DataBase'

    def handle(self, *args, **options):
        with open('recipes/data/ingredients.csv') as file:
            file_reader = csv.reader(file)
            ProductCategory.objects.all().delete()
            Ingredient.objects.all().delete()
            for row in file_reader:
                row_list = row[0].split(';')
                name = row_list[0]
                unit = row_list[1]
                category_name = row_list[2]
                category = ProductCategory.objects.get_or_create(name=category_name)[0]
                ingredient = Ingredient(name=name, unit=unit, category=category)
                ingredient.save()
