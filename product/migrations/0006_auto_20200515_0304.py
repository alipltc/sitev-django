# Generated by Django 3.0.6 on 2020-05-15 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200515_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeri',
            name='title',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]
