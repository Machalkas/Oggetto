# Generated by Django 3.1.7 on 2021-03-20 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0004_auto_20210320_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='logo',
            field=models.ImageField(upload_to='logo', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
