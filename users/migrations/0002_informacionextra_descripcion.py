# Generated by Django 4.2 on 2023-06-04 21:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionextra',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
