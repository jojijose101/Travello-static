# Generated by Django 4.2.5 on 2023-09-14 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='photo',
            new_name='place',
        ),
    ]