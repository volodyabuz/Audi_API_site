# Generated by Django 4.2.9 on 2024-04-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiapi', '0002_alter_carmodels_options_alter_generations_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['id'], 'verbose_name': 'автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos/%Y/%m/%d/', verbose_name='Фото от пользователя'),
        ),
    ]
