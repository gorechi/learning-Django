from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, TextField, URLField, DateTimeField, ForeignKey, SmallIntegerField, BooleanField, ManyToManyField

# Create your models here.
class District(Model):
    name = CharField(max_length=200)
    description = TextField(null=True, blank=True)
    creation_date = DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
    
class Location(Model):
    name = CharField(max_length=200)
    description = TextField(null=True, blank=True)
    creation_date = DateTimeField(auto_now_add = True)
    district = ForeignKey(
        District, 
        on_delete=models.CASCADE, 
        related_name='locations', 
        related_query_name='location'
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

class Place (Model):
    PLACE_TYPES = (
        (None, 'Выберите тип шаурмичной'),
        (1, 'Кафе'),
        (2, 'Ларек'),
        (3, 'Фудтрак'),
    )
    
    name = CharField(max_length=200, verbose_name='Название')
    description = TextField(blank=True, null=True, verbose_name='Описание')
    url = URLField(blank=True, null=True, verbose_name='Адрес сайта')
    creation_date = DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    address = CharField(max_length=300, blank=True, null=True, verbose_name='Адрес')
    location = ForeignKey(
        Location, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='places', 
        related_query_name='place',
        verbose_name='Расположение'
        )
    place_type = SmallIntegerField(choices=PLACE_TYPES, verbose_name='Тип')
    phone = CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    delivery = BooleanField(default=False, verbose_name='Есть доставка')
    seats = BooleanField(default=False, verbose_name='Есть столики')
    toilet = BooleanField(default=False, verbose_name='Есть туалет')
    parking = BooleanField(default=False, verbose_name='Есть парковка')
    order_by_phone = BooleanField(default=False, verbose_name='Можно заказать по телефону')
    
    def __str__(self):
        return f'{self.name}, {self.location.name}'
    
    def clean(self):
        errors = {}
        if not self.name:
            errors['name'] = ValidationError('Укажите имя шаурмичной')
        if errors:
            raise ValidationError(errors)
    
    class Meta:
        verbose_name = 'Шаурмичная'
        verbose_name_plural = 'Шаурмичные'
        ordering = ['-creation_date']
    
class PlaceRate(Model):
    place = ForeignKey(
        Place,
        on_delete=models.CASCADE, 
        related_name='rates', 
        related_query_name='rate'
        )
    rate = SmallIntegerField()
    creation_date = DateTimeField(auto_now_add=True)
    change_date = DateTimeField(auto_now=True)
    
    def __str__(self):
        stars = self.rate * '*'
        return f'[Шаурмичная: {self.place.name}, Оценка: {stars}]'
    
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        ordering = ['-creation_date']
        

class Ingredient (Model):
    name = CharField(max_length=200, verbose_name='Название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        
class Shawa (Model):
    
    SHAWA_TYPES = (
        (None, 'Выберите тип шаурмы'),
        (1, 'Классическая'),
        (2, 'Сырная'),
        (3, 'Острая'),
    )
    
    SHAWA_MEAT = (
        (None, 'Выберите мясо'),
        (1, 'С говядиной'),
        (2, 'Со свининой'),
        (3, 'С курицей'),
        (4, 'С бараниной'),
        (5, 'Со свининой и говядиной'),
    )
    
    SHAWA_SIZES = (
        (None, 'Выберите размер'),
        (1, 'Огромная'),
        (2, 'Большая'),
        (3, 'Стандартная'),
        (4, 'Маленькая'),
    )
    
    name = CharField(max_length=200, verbose_name='Название')
    description = TextField(blank=True, null=True, verbose_name='Описание')
    shawa_type = SmallIntegerField(choices=SHAWA_TYPES, verbose_name='Тип')
    meat = SmallIntegerField(choices=SHAWA_MEAT, verbose_name='Мясо')
    size = SmallIntegerField(choices=SHAWA_SIZES, verbose_name='Размер')
    creation_date = DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    place = ForeignKey(
        Place,
        on_delete=models.CASCADE, 
        related_name='shawas', 
        related_query_name='shawa'
        )
    spicy = BooleanField(default=False, verbose_name='Острая')
    ingredients = ManyToManyField(
        Ingredient,
        related_name='shawas', 
        related_query_name='shawa'
        )
    
    def save(self, *args, **kwargs):
        if self.shawa_type == 3:
            self.spicy = True
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def full_name(self):
        shawa_type = self.get_shawa_type_display().lower()
        shawa_size = self.get_size_display().lower()
        shawa_meat = self.get_meat_display().lower()
        return f'{self.name}, {shawa_type} {shawa_size} {shawa_meat}'
    
    class Meta:
        verbose_name = 'Шаурма'
        verbose_name_plural = 'Шавухи'
        unique_together = ('place', 'shawa_type', 'meat', 'size')
        ordering = ['-creation_date']
