# Generated by Django 4.0.2 on 2022-02-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes_and_villains', '0006_rename_super_type_id_super_super_type'),
        ('type_heroes_or_villains', '0011_rename_alignment_super_type_type_alter_super_type_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Super_type',
            new_name='SuperType',
        ),
    ]
