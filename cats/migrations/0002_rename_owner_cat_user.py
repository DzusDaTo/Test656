# Generated by Django 5.1.2 on 2024-10-08 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='owner',
            new_name='user',
        ),
    ]
