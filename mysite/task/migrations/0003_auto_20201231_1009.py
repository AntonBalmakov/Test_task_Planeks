# Generated by Django 3.0.7 on 2020-12-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20201231_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstusermodel',
            name='count',
            field=models.IntegerField(choices=[('Предложения', '1'), ('Предложения', '2'), ('Предложения', '3'), ('Предложения', '4')], null=True, verbose_name='count'),
        ),
    ]
