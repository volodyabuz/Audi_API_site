from django.db import models
from django.utils.translation import gettext_lazy as _

#Классы об автомобилях

class Cars(models.Model):
    '''Конкретный автомобиль из существующих.'''

    name = models.CharField(max_length=50, db_index=True, verbose_name='Модель')
    about = models.TextField(blank=True, verbose_name='Об автомобиле')
    generation = models.ForeignKey('Generations', on_delete=models.CASCADE)
    motor = models.ForeignKey('Motors', on_delete=models.CASCADE)
    gearbox = models.ForeignKey('Gearboxes', on_delete=models.CASCADE)
    car_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото автомобиля')

    def __str__(self):
        return self.name

class Generations(models.Model):
    '''Поколения автомобилей.'''

    name = models.ForeignKey('Cars', on_delete=models.PROTECT)
    gen = models.CharField(max_length=10, verbose_name='Поколение')

    def __str__(self) -> str:
        return self.gen


class Motors(models.Model):
    '''Типы двигателей их их модели.'''

    class FuelCategory(models.TextChoices):
        '''Тип топлива.'''

        PETROL = "PT", _('Бензин')
        DIESEL = "DT", _('Дизель')
        HYBRID = "HB", _('Гибрид')

    gen = models.ForeignKey('Generations', on_delete=models.CASCADE)
    fuel = models.CharField(max_length=2, choices=FuelCategory, default=FuelCategory.PETROL, verbose_name='Тип двигателя')
    engine = models.CharField(db_index=True, verbose_name='Двигатель')
    gear = models.ForeignKey('Gearboxes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.engine

class Gearboxes(models.Model):
    '''Типы коробок передач.'''

    class WheelDrive(models.TextChoices):
        '''Типы привода колес.'''

        FWD = "FWD", _('Передний')
        RWD = "RWD", _('Задний')
        AWD = "AWD", _('Полный')

    gear = models.CharField(db_index=True, unique=True, verbose_name='Коробка передач')
    wd = models.CharField(max_length=3, choices=WheelDrive, default=WheelDrive.FWD, verbose_name='Привод')

    def __str__(self) -> str:
        return self.gear


#Классы о пользователях

class Garage(models.Model):
    '''Гараж пользователя.'''

    user = models.ForeignKey('users', on_delete=models.PROTECT)
    my_car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    get_recomm = models.BooleanField(default=True, verbose_name='Получать рекомендации')

class Recommendations(models.Model):
    '''Рекомендации объявлений для пользователя.'''

    car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    url = models.TextField(blank=True, verbose_name='Объявление')
    time_shared = models.DateTimeField(auto_now=True, verbose_name='Время размещения')

class Comments(models.Model):
    '''Комментарии пользователей о модели автомобиля.'''

    user = models.ForeignKey('users', on_delete=models.PROTECT)
    car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    users_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото от пользователя')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
