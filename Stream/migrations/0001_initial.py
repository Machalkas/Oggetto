# Generated by Django 3.1.7 on 2021-03-19 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, null=True, unique=True, verbose_name='Токен')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.shop', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Стрим',
                'verbose_name_plural': 'Стримы',
            },
        ),
    ]
