# Generated by Django 3.0.6 on 2020-05-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200530_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]