# Generated by Django 4.1.4 on 2022-12-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField()),
                ('status', models.CharField(max_length=12)),
                ('veg_images', models.ImageField(upload_to='veg_images')),
            ],
        ),
    ]
