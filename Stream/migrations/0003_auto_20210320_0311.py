# Generated by Django 3.1.7 on 2021-03-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stream', '0002_auto_20210320_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='token',
        ),
        migrations.AddField(
            model_name='stream',
            name='url',
            field=models.URLField(default=None, null=True, verbose_name='Ссылка'),
        ),
    ]
