# Generated by Django 4.0.2 on 2022-02-18 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type_heroes_or_villains', '0003_rename_status_super_type_alignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super_type',
            name='alignment',
        ),
    ]