# Generated by Django 3.0.6 on 2020-05-12 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200513_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]