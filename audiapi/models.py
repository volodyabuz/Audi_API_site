from django.db import models
from django.contrib.auth.models import User


#Классы об автомобилях

class Cars(models.Model):
    '''Конкретный автомобиль из существующих.'''

    name = models.ForeignKey('CarModels', on_delete=models.CASCADE, verbose_name='Модель')
    generation = models.ForeignKey('Generations', on_delete=models.CASCADE, verbose_name='Поколение')
    body_type = models.ForeignKey('BodyTypes', on_delete=models.CASCADE, verbose_name='Тип кузова')
    fuel_type = models.ForeignKey('FuelTypes', on_delete=models.CASCADE, verbose_name='Топливо')
    motor = models.ForeignKey('Motors', on_delete=models.CASCADE, verbose_name='Двигатель')
    gearbox = models.ForeignKey('Gearboxes', on_delete=models.CASCADE, verbose_name='Коробка передач')
    wheel_drive = models.ForeignKey('WheelDrives', on_delete=models.CASCADE, verbose_name='Привод')
    about = models.TextField(blank=True, verbose_name='Об автомобиле')
    car_photo = models.ImageField(upload_to="car_photos/%Y/%m/%d/", verbose_name='Фото автомобиля')

    def __str__(self):
        return f'{self.name}, {self.generation}'

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'Автомобили'


class CarModels(models.Model):
    '''Модель автомобиля.'''

    car_name = models.CharField(max_length=50, db_index=True, verbose_name='Модель')

    def __str__(self) -> str:
        return self.car_name

    class Meta:
        verbose_name = 'модель Audi'
        verbose_name_plural = 'Модели Audi'
        ordering = ['car_name',]


class Generations(models.Model):
    '''Поколения автомобилей.'''

    model_name = models.ForeignKey('CarModels', on_delete=models.CASCADE, verbose_name='Модель')
    gen = models.CharField(max_length=50, verbose_name='Поколение')

    def __str__(self) -> str:
        return f'{self.model_name}, {self.gen}'

    class Meta:
        verbose_name = 'поколение'
        verbose_name_plural = 'Поколения'


class BodyTypes(models.Model):
    '''Типы кузова автомобиля.'''

    # BODY_TYPE_CHOICES = [
    #     ('HT3', 'Хэтчбек 3дв.'),
    #     ('HT5', 'Хэтчбек 5дв.'),
    #     ('SD4', 'Седан 4дв.'),
    #     ('UV5', 'Универсал 5дв.'),
    #     ('SV5', 'Внедорожник 5дв.'),
    #     ('CU2', 'Купэ 2дв.'),
    #     ('CB2', 'Кабриолет 2дв.'),
    # ]

    body = models.CharField(max_length=20, verbose_name='Тип кузова')

    def __str__(self) -> str:
        return self.body

    class Meta:
        verbose_name = 'тип кузова'
        verbose_name_plural = 'Типы кузова'


class FuelTypes(models.Model):
    '''Типы топлива двигателя.'''

    # FUEL_CHOICES = [
    #     ("PT", 'Бензин'),
    #     ("DT", 'Дизель'),
    #     ("HB", 'Гибрид'),
    #     ("EL", 'Электро')
    # ]

    fuel = models.CharField(max_length=10, default='Бензин', verbose_name='Тип двигателя')

    def __str__(self) -> str:
        return self.fuel

    class Meta:
        verbose_name = 'тип топлива'
        verbose_name_plural = 'Типы топлива'


class Motors(models.Model):
    '''Модели двигателя автомобиля.'''

    gen = models.ForeignKey('Generations', on_delete=models.CASCADE, verbose_name='Поколение')
    engine = models.CharField(db_index=True, verbose_name='Двигатель')

    def __str__(self) -> str:
        return self.engine

    class Meta:
        verbose_name = 'двигатель'
        verbose_name_plural = 'Двигатели'


class Gearboxes(models.Model):
    '''Типы коробок передач.'''

    # GEARBOX_CHOICES = [
    #     ("MT", 'Механика'),
    #     ("AT", 'Автомат'),
    #     ("AMT", 'Робот'),
    #     ("CVT", 'Вариатор')
    # ]

    gear = models.CharField(max_length=10, default='Механика', verbose_name='Коробка передач')

    def __str__(self) -> str:
        return self.gear
    
    class Meta:
        verbose_name = 'коробку передач'
        verbose_name_plural = 'Коробки передач'
        ordering = ['id',]


class WheelDrives(models.Model):
    '''Типы привода автомобиля.'''

    # WHEELDRIVE_CHOICES = [
    #     ("FWD", 'Передний'),
    #     ("RWD", 'Задний'),
    #     ("AWD", 'Полный')
    # ]

    wd = models.CharField(max_length=10, default='Передний', verbose_name='Привод')

    def __str__(self) -> str:
        return self.wd

    class Meta:
        verbose_name = 'тип привода'
        verbose_name_plural = 'Типы привода'


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
    url_photo = models.ImageField(upload_to="url_photos/%Y/%m/%d/", verbose_name='Фото объявления')
    shared_time = models.DateTimeField(auto_now=True, verbose_name='Время размещения')

    class Meta:
        verbose_name = 'Рекомендации'
        verbose_name_plural = 'Рекомендации'


class Comments(models.Model):
    '''Комментарии пользователей о модели автомобиля.'''

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    user_photo = models.ImageField(upload_to="user_photos/%Y/%m/%d/", verbose_name='Фото от пользователя')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
