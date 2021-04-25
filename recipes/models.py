from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .common_fields import FieldSlug, FieldVisible, FieldUpdated, FieldSorting, \
    FieldCreated, FieldImage, FieldSEO, FieldAuthor


User = get_user_model()


# Create your models here.
class ProductCategory(FieldSlug, FieldVisible, FieldUpdated, FieldCreated, FieldSorting):
    name = models.CharField(
        max_length=100,
        verbose_name=_('name of the product category'),  # Название категории продуктов
        blank=False,
    )

    class Meta:
        verbose_name = _('category of products')
        verbose_name_plural = _('categories of products')
        app_label = 'recipes'
        ordering = ('sorting',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug})


class Ingredient(FieldCreated, FieldSorting):
    name = models.CharField(
        max_length=100,
        verbose_name=_('name of the ingredient'),  # Название ингидиента
        blank=False,
        db_index=True
    )
    unit = models.CharField(
        max_length=20,
        verbose_name=_('unit of measurement')  # единица измерения
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('ingredient')
        verbose_name_plural = _('ingredients')
        app_label = 'recipes'
        ordering = ('sorting',)

    def __str__(self):
        return f'{self.name}, {self.unit}'


class Recipe(FieldSlug, FieldImage, FieldVisible, FieldUpdated, FieldCreated, FieldSorting):
    MEAL_TIME = (
        ('0', 'Завтрак'),
        ('1', 'Обед'),
        ('2', 'Ужин'),
    )
    tittle = models.CharField(
        max_length=100,
        verbose_name=_('name of the recipe'),  # Название рецепта
        blank=False,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.CASCADE
    )
    content = models.TextField(
        verbose_name=_('content'),
        null=True,
        blank=True
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='RecipeIngredients',
        verbose_name=_('ingredients of recipe'),  # список ингедиентов
    )
    teg = models.CharField(
        choices=MEAL_TIME,
        max_length=20,
        verbose_name=_('meal time'),  # время приёма пищи
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name=_('cooking time')  # время приготовления
    )

    class Meta:
        verbose_name = _('recipe')
        verbose_name_plural = _('recipes')
        app_label = 'recipes'
        ordering = ('sorting',)

    def __str__(self):
        return self.tittle


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name=_('quantity')  # количество
    )

    class Meta:
        verbose_name = _('ingredients of recipe')  # список ингедиентов
        verbose_name_plural = _('ingredients of recipe')
        app_label = 'recipes'
