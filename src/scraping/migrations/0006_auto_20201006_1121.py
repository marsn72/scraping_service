# Generated by Django 3.0.10 on 2020-10-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_auto_20201006_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название населенного пункта'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Язык программирования'),
        ),
    ]
