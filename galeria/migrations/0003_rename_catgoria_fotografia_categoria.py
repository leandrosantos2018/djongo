# Generated by Django 4.1 on 2024-06-23 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_catgoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='catgoria',
            new_name='categoria',
        ),
    ]
