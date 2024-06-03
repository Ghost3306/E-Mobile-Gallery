# Generated by Django 5.0.6 on 2024-06-03 07:08

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_phoneimages_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraDetails',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('camera_name', models.CharField(max_length=30)),
                ('camera_mp', models.IntegerField()),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camera', to='products.phonelist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]