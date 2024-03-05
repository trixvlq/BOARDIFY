from django.db import models
from Users.models import User


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Town(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название города')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Продавец')
    price = models.IntegerField(verbose_name='Цена продукта')
    image = models.ImageField(upload_to='static/images/%Y/%m/%d/')
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_created=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name='Город')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
