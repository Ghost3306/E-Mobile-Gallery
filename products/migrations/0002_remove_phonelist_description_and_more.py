# Generated by Django 5.0.6 on 2024-05-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonelist',
            name='description',
        ),
        migrations.AlterField(
            model_name='cpuspecs',
            name='cpu_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='additional',
            field=models.ManyToManyField(to='products.additionaldetails'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='battery',
            field=models.ManyToManyField(to='products.batterydetails'),
        ),
        migrations.RemoveField(
            model_name='phonelist',
            name='cellular_net',
        ),
        migrations.RemoveField(
            model_name='phonelist',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='phonelist',
            name='connectivity',
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='cpu',
            field=models.ManyToManyField(to='products.cpuspecs'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='display',
            field=models.ManyToManyField(to='products.display'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='front_camera',
            field=models.ManyToManyField(to='products.frontcamera'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='inthebox',
            field=models.ManyToManyField(to='products.inthebox'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='ram_rom',
            field=models.ManyToManyField(to='products.ramrom'),
        ),
        migrations.AlterField(
            model_name='phonelist',
            name='rear_camera',
            field=models.ManyToManyField(to='products.rearcamera'),
        ),
        migrations.AddField(
            model_name='phonelist',
            name='cellular_net',
            field=models.ManyToManyField(to='products.cellularnetwork'),
        ),
        migrations.AddField(
            model_name='phonelist',
            name='colors',
            field=models.ManyToManyField(to='products.color'),
        ),
        migrations.AddField(
            model_name='phonelist',
            name='connectivity',
            field=models.ManyToManyField(to='products.connectivity'),
        ),
    ]
