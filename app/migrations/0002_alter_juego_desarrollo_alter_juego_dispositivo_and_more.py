# Generated by Django 4.2 on 2023-04-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='desarrollo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='juego',
            name='dispositivo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='juego',
            name='genero',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='juego',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]