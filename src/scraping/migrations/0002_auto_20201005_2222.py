# Generated by Django 3.0.10 on 2020-10-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название населенного пункта'),
        ),
    ]