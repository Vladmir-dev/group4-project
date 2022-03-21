# Generated by Django 4.0.3 on 2022-03-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='')),
                ('body', models.CharField(max_length=2000)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
