# Generated by Django 4.0.3 on 2022-10-08 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='create_date',
        ),
    ]
