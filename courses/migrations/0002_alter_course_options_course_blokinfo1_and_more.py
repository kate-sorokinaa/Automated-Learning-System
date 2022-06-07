# Generated by Django 4.0.5 on 2022-06-07 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AddField(
            model_name='course',
            name='blokInfo1',
            field=models.TextField(default='', verbose_name='Блок с информацией 1'),
        ),
        migrations.AddField(
            model_name='course',
            name='blokInfo2',
            field=models.TextField(default='', verbose_name='Блок с информацией 2'),
        ),
        migrations.AddField(
            model_name='course',
            name='blokInfo3',
            field=models.TextField(default='', verbose_name='Блок с информацией 3'),
        ),
    ]