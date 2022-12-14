# Generated by Django 4.0.3 on 2022-10-10 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0005_alter_menu_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='voter',
            field=models.ManyToManyField(related_name='voter_menu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='menu',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_menu', to=settings.AUTH_USER_MODEL),
        ),
    ]
