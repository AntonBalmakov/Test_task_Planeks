# Generated by Django 3.0.7 on 2020-12-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='first name')),
                ('last_name', models.CharField(max_length=32, verbose_name='last name')),
                ('Job', models.CharField(max_length=32, verbose_name='Job')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='email')),
                ('domain_name', models.CharField(max_length=32, verbose_name='domain name')),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone number')),
                ('company_name', models.CharField(max_length=32, verbose_name='company name')),
                ('order', models.CharField(choices=[('0', 'Предложения'), ('1', 'Предложений'), ('2', 'Предложений'), ('3', 'Предложений')], max_length=32, verbose_name='order')),
                ('count', models.IntegerField(choices=[('1', 'Предложение'), ('2', 'Предложение'), ('3', 'Предложение')], max_length=10)),
                ('address', models.CharField(max_length=32, verbose_name='address')),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
