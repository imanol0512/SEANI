# Generated by Django 5.0.2 on 2024-02-27 19:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_question_question_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagen de la Pregunta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(blank=True, null=True, verbose_name='Texto de la Pregunta'),
        ),
    ]
