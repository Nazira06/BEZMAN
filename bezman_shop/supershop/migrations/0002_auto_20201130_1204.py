# Generated by Django 3.1.3 on 2020-11-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supershop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='123.png', upload_to=''),
        ),
    ]
