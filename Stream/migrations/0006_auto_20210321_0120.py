# Generated by Django 3.1.7 on 2021-03-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stream', '0005_stream_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='url',
            field=models.CharField(default=None, max_length=250, null=True, verbose_name='Ссылка'),
        ),
    ]
