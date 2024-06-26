# Generated by Django 5.0.6 on 2024-06-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_address_placedorders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='locality',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='taluka',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='village_city',
            field=models.CharField(max_length=100),
        ),
    ]
