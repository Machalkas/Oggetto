# Generated by Django 3.1.7 on 2021-03-20 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_auto_20210320_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.shop', verbose_name='Магазин'),
        ),
    ]
