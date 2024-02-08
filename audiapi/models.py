from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

#Классы об автомобилях

class Cars(models.Model):
    '''Конкретный автомобиль из существующих.'''

    name = models.ForeignKey('Generations', on_delete=models.CASCADE, verbose_name='Модель')
    about = models.TextField(blank=True, verbose_name='Об автомобиле')
    motor = models.ForeignKey('Motors', on_delete=models.CASCADE)
    gearbox = models.ForeignKey('Gearboxes', on_delete=models.CASCADE)
    car_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото автомобиля')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобили'
        verbose_name_plural = 'Автомобили'


class Generations(models.Model):
    '''Поколения автомобилей.'''

    BODY_TYPE_CHOICES = [
        ('HT3', 'Хэтчбек 3дв.'),
        ('HT5', 'Хэтчбек 5дв.'),
        ('SD4', 'Седан 4дв.'),
        ('UV5', 'Универсал 5дв.'),
        ('SV5', 'Внедорожник 5дв.'),
        ('CU2', 'Купэ 2дв.'),
        ('CB2', 'Кабриолет 2дв.'),
    ]

    car_name = models.CharField(max_length=50, db_index=True, verbose_name='Модель')
    gen = models.CharField(max_length=50, verbose_name='Поколение')
    body = models.CharField(max_length=3, choices=BODY_TYPE_CHOICES, verbose_name='Тип кузова')


    def __str__(self) -> str:
        return self.gen

    class Meta:
        verbose_name = 'Поколения автомобилей'
        verbose_name_plural = 'Поколения автомобилей'


class Motors(models.Model):
    '''Типы двигателей их их модели.'''

    FUEL_CHOICES = [
        ("PT", 'Бензин'),
        ("DT", 'Дизель'),
        ("HB", 'Гибрид')
    ]

    gen = models.ForeignKey('Generations', on_delete=models.CASCADE)
    fuel = models.CharField(max_length=2, choices=FUEL_CHOICES, default=FUEL_CHOICES[0], verbose_name='Тип двигателя')
    engine = models.CharField(db_index=True, verbose_name='Двигатель')
    gear = models.ForeignKey('Gearboxes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.engine

    class Meta:
        verbose_name = 'Двигатели'
        verbose_name_plural = 'Двигатели'

class Gearboxes(models.Model):
    '''Типы коробок передач.'''

    WHEELDRIVE_CHOICES = [
        ("FWD", 'Передний'),
        ("RWD", 'Задний'),
        ("AWD", 'Полный')
    ]

    gear = models.CharField(db_index=True, verbose_name='Коробка передач')
    wd = models.CharField(max_length=3, choices=WHEELDRIVE_CHOICES, default=WHEELDRIVE_CHOICES[0], verbose_name='Привод')

    def __str__(self) -> str:
        return self.gear
    
    class Meta:
        verbose_name = 'Коробки передач'
        verbose_name_plural = 'Коробки передач'
        ordering = ['id',]


#Классы о пользователях

class Garage(models.Model):
    '''Гараж пользователя.'''

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    my_car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    get_recomm = models.BooleanField(default=True, verbose_name='Получать рекомендации')

    class Meta:
        verbose_name = 'Гараж'
        verbose_name_plural = 'Гараж'


class Recommendations(models.Model):
    '''Рекомендации объявлений для пользователя.'''

    car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    url = models.TextField(blank=True, verbose_name='Объявление')
    time_shared = models.DateTimeField(auto_now=True, verbose_name='Время размещения')

    class Meta:
        verbose_name = 'Рекомендации'
        verbose_name_plural = 'Рекомендации'


class Comments(models.Model):
    '''Комментарии пользователей о модели автомобиля.'''

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    users_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото от пользователя')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
