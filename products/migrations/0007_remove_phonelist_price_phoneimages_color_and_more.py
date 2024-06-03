# Generated by Django 5.0.6 on 2024-06-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_cameradetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonelist',
            name='price',
        ),
        migrations.AddField(
            model_name='phoneimages',
            name='color',
            field=models.CharField(default='color', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phoneimages',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
