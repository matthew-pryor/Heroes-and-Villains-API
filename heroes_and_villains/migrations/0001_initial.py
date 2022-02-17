# Generated by Django 4.0.2 on 2022-02-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alter_ego', models.CharField(max_length=255)),
                ('primary_ability', models.CharField(max_length=255)),
                ('secondary_ability', models.CharField(max_length=255)),
                ('catchphrase', models.CharField(max_length=999)),
                ('super_type_id', models.IntegerField(choices=[(1, 'Hero'), (2, 'Villain')])),
            ],
        ),
    ]