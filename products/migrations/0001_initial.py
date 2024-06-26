# Generated by Django 5.0.6 on 2024-05-21 15:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalDetails',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('weight', models.FloatField()),
                ('country_of_origin', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BatteryDetails',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('capacity', models.IntegerField()),
                ('charging_speed', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('brand_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('brand_logo', models.ImageField(upload_to='brands')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CameraFeatures',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('feature', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category_image', models.ImageField(upload_to='categories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CellularNetwork',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('network_type', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('color_name', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Connectivity',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('connectivity_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CPUSpecs',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cpu_name', models.CharField(max_length=50)),
                ('cpu_speed', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('display_name', models.CharField(max_length=20)),
                ('resolution_x', models.IntegerField()),
                ('resolution_y', models.IntegerField()),
                ('display_size', models.FloatField()),
                ('pixel_per_inch', models.IntegerField()),
                ('hz', models.IntegerField()),
                ('touch_response', models.IntegerField()),
                ('color_depth', models.CharField(max_length=20)),
                ('brightness', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FrontCamera',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('front_camera_name', models.CharField(default='standard', max_length=50)),
                ('front_camera_mp', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InTheBox',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('items', models.CharField(max_length=25)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OSDetails',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('os_name', models.CharField(max_length=25)),
                ('os_version', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RamRom',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('ram_size', models.IntegerField()),
                ('rom_size', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneList',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('phone_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('additional', models.ManyToManyField(null=True, to='products.additionaldetails')),
                ('battery', models.ManyToManyField(null=True, to='products.batterydetails')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='brand', to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='products.category')),
                ('cellular_net', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cellularname', to='products.cellularnetwork')),
                ('colors', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='colors', to='products.color')),
                ('connectivity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='connectivity', to='products.connectivity')),
                ('cpu', models.ManyToManyField(null=True, to='products.cpuspecs')),
                ('display', models.ManyToManyField(null=True, to='products.display')),
                ('front_camera', models.ManyToManyField(null=True, to='products.frontcamera')),
                ('inthebox', models.ManyToManyField(null=True, to='products.inthebox')),
                ('os_details', models.ManyToManyField(blank=True, to='products.osdetails')),
                ('ram_rom', models.ManyToManyField(null=True, to='products.ramrom')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneImages',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_images', to='products.phonelist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RearCamera',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('rear_primary_camera_name', models.CharField(default='standard', max_length=50)),
                ('rear_primary_camera_mp', models.IntegerField()),
                ('rear_macro_camera_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rear_macro_camera_mp', models.IntegerField(blank=True, null=True)),
                ('rear_telephoto_camera_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rear_telephoto_camera_mp', models.IntegerField(blank=True, null=True)),
                ('rear_ultrawide_camera_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rear_ultrawide_camera_mp', models.IntegerField(blank=True, null=True)),
                ('flash_type', models.CharField(max_length=20)),
                ('ois', models.BooleanField(default=False)),
                ('eis', models.BooleanField(default=False)),
                ('features', models.ManyToManyField(blank=True, to='products.camerafeatures')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='phonelist',
            name='rear_camera',
            field=models.ManyToManyField(null=True, to='products.rearcamera'),
        ),
    ]
