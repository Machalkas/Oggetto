# Generated by Django 3.1.7 on 2021-03-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20210320_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='Логотип'),
        ),
    ]