# Generated by Django 4.2.4 on 2024-05-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0005_alter_properties_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='properties',
            name='images',
            field=models.ImageField(upload_to='properties'),
        ),
    ]
