# Generated by Django 4.2.9 on 2024-05-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiapi', '0004_generations_drom_gen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendations',
            name='url_photo',
            field=models.ImageField(blank=True, upload_to='url_photos/%Y/%m/%d/', verbose_name='Фото объявления'),
        ),
    ]
