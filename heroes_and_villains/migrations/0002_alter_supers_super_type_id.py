# Generated by Django 4.0.2 on 2022-02-18 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('type_heroes_or_villains', '0001_initial'),
        ('heroes_and_villains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supers',
            name='super_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='type_heroes_or_villains.super_type'),
        ),
    ]
