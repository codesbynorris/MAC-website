# Generated by Django 4.2.19 on 2025-02-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macapp', '0006_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='category',
            field=models.CharField(default=21, max_length=25, verbose_name='Product Category'),
            preserve_default=False,
        ),
    ]
