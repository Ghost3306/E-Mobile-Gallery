# Generated by Django 5.0.6 on 2024-05-21 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_verifiedv',
            new_name='is_verified',
        ),
    ]