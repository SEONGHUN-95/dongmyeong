# Generated by Django 4.0.3 on 2022-10-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.CharField(max_length=11),
        ),
    ]
