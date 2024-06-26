# Generated by Django 4.2.4 on 2024-05-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('size', models.CharField(blank=True, max_length=50)),
                ('bedrooms', models.IntegerField(blank=True)),
                ('bathrooms', models.IntegerField(blank=True)),
                ('amentities', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('year_built', models.IntegerField()),
                ('images', models.ImageField(upload_to='images/properties')),
                ('location', models.CharField(max_length=100)),
                ('features', models.TextField(blank=True)),
            ],
        ),
    ]
