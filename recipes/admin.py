from django.contrib import admin
from django.contrib.admin.decorators import register
from django.utils.translation import gettext_lazy as _

from .models import ProductCategory, Ingredient, RecipeIngredients, Recipe


# Register your models here.
@register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'is_visible', 'sorting',)
    list_editable = ('is_visible', 'sorting',)
    list_filter = ('is_visible',)
    search_fields = ('name',)
    readonly_fields = ('created', 'updated',)
    save_on_top = True

    fieldsets = (
        (_('page params'),
         {'fields': ('name', 'sorting', 'is_visible', 'created', 'updated',)}),
    )


@register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'category', 'created', 'sorting',)
    list_editable = ('sorting',)
    list_filter = ('category',)
    search_fields = ('name',)
    readonly_fields = ('created',)
    save_on_top = True

    fieldsets = (
        (_('page params'),
         {'fields': ('name', 'unit', 'category', 'sorting', 'created',)}),
    )


class RecipeIngredientsInLines(admin.TabularInline):
    model = RecipeIngredients


@register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'cooking_time', 'is_visible', 'created', 'sorting',)
    list_editable = ('is_visible', 'sorting',)
    list_filter = ('teg',)
    search_fields = ('tittle',)
    readonly_fields = ('created',)
    save_on_top = True

    fieldsets = (
        (_('page params'),
         {'fields': (('tittle', 'cooking_time',),
                     ('teg', 'author',),
                     'content', 'image',
                     'is_visible', 'sorting', 'created',)
          }),
    )
    inlines = (RecipeIngredientsInLines,)
