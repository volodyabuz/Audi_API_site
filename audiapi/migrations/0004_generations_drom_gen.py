# Generated by Django 4.2.9 on 2024-05-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiapi', '0003_alter_cars_options_alter_comments_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='generations',
            name='drom_gen',
            field=models.CharField(blank=True, max_length=50, verbose_name='Поколение для Drom'),
        ),
    ]
