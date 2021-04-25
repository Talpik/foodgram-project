# Generated by Django 3.2 on 2021-04-25 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import foodgram.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('sorting', models.PositiveIntegerField(default=0, verbose_name='sorting')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name of the ingredient')),
                ('unit', models.CharField(max_length=20, verbose_name='unit of measurement')),
            ],
            options={
                'verbose_name': 'ingredient',
                'verbose_name_plural': 'ingredients',
                'ordering': ('sorting',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=100, unique=True, verbose_name='slug')),
                ('is_visible', models.BooleanField(default=True, verbose_name='is visible')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('sorting', models.PositiveIntegerField(default=0, verbose_name='sorting')),
                ('name', models.CharField(max_length=100, verbose_name='name of the product category')),
            ],
            options={
                'verbose_name': 'category of products',
                'verbose_name_plural': 'categories of products',
                'ordering': ('sorting',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid1, max_length=100, unique=True, verbose_name='slug')),
                ('is_visible', models.BooleanField(default=True, verbose_name='is visible')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('sorting', models.PositiveIntegerField(default=0, verbose_name='sorting')),
                ('image', models.ImageField(help_text='image size no more than 1920х960px', upload_to=foodgram.utils.ImageUploadToFactory('images'), verbose_name='image')),
                ('tittle', models.CharField(db_index=True, max_length=100, verbose_name='name of the recipe')),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('teg', models.CharField(choices=[(0, 'Завтрак'), (1, 'Обед'), (2, 'Ужин')], max_length=20, verbose_name='meal time')),
                ('cooking_time', models.PositiveIntegerField(verbose_name='cooking time')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'recipe',
                'verbose_name_plural': 'recipes',
                'ordering': ('sorting',),
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
            options={
                'verbose_name': 'ingredients of recipe',
                'verbose_name_plural': 'ingredients of recipe',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.RecipeIngredients', to='recipes.Ingredient', verbose_name='ingredients of recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.productcategory'),
        ),
    ]
