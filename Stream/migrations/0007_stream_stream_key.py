# Generated by Django 3.1.7 on 2021-03-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stream', '0006_auto_20210321_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='stream_key',
            field=models.CharField(default='', max_length=25, verbose_name='StreamKey'),
        ),
    ]