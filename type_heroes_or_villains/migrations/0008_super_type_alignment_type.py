# Generated by Django 4.0.2 on 2022-02-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type_heroes_or_villains', '0007_super_type_alignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='super_type',
            name='alignment_type',
            field=models.CharField(default='Hero', max_length=255),
            preserve_default=False,
        ),
    ]
