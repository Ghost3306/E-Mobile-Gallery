# Generated by Django 5.0.6 on 2024-05-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_phonelist_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneimages',
            name='color',
            field=models.ManyToManyField(to='products.color'),
        ),
    ]