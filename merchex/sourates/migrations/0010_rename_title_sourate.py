# Generated by Django 4.2.7 on 2024-01-17 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sourates', '0009_alter_date_date_jour'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='Sourate',
        ),
    ]
