# Generated by Django 4.2.4 on 2024-05-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0006_properties_featured_alter_properties_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='images',
            field=models.FileField(upload_to='properties'),
        ),
    ]
