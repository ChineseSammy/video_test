# Generated by Django 2.1.2 on 2021-09-30 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientuser',
            old_name='create_time',
            new_name='created_time',
        ),
    ]