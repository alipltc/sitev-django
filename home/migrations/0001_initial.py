# Generated by Django 3.0.6 on 2020-05-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('smtpserver', models.CharField(max_length=20)),
                ('smtpemail', models.CharField(max_length=20)),
                ('smtppassword', models.CharField(max_length=20)),
                ('smtpport', models.CharField(max_length=5)),
                ('icon', models.ImageField(blank=True, max_length=5, upload_to='')),
                ('facebook', models.CharField(max_length=60)),
                ('instagram', models.CharField(max_length=60)),
                ('twitter', models.CharField(max_length=60)),
                ('aboutus', models.TextField()),
                ('referans', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
