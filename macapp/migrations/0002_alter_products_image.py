# Generated by Django 5.1.6 on 2025-02-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Image'),
        ),
    ]
