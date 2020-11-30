# Generated by Django 3.1.3 on 2020-11-30 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('product_type', models.CharField(choices=[('classic', 'classic'), ('sport', 'sport'), ('dm', 'demi-season'), ('winter', 'winter')], max_length=40)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('uni', 'uni')], max_length=20)),
                ('product_model', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=15)),
                ('size', models.CharField(choices=[('child', 'child'), ('medium', 'medium'), ('large', 'large'), ('XL', 'XL')], max_length=20)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
