# Generated by Django 5.0.3 on 2024-05-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='popularDestinaion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='PopularDestination')),
                ('nameOfImage', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
            ],
        ),
    ]