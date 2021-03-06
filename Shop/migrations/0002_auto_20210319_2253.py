# Generated by Django 3.1.7 on 2021-03-19 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Stream', '0001_initial'),
        ('Shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='goods',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.shop', verbose_name='Магазин'),
        ),
        migrations.AddField(
            model_name='goods',
            name='stream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Stream.stream', verbose_name='Стрим'),
        ),
    ]
