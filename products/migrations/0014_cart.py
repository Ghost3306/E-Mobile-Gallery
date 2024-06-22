# Generated by Django 5.0.6 on 2024-06-22 14:54

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_display_display_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='phonename_id', to='products.phonelist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='username_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
