# Generated by Django 4.1.5 on 2023-01-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_restaurant_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='amountCurrency',
            field=models.CharField(choices=[('KZT', 'Kzt'), ('USD', 'Usd'), ('RUB', 'Rub')], default='KZT', max_length=3),
        ),
    ]