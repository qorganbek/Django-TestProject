# Generated by Django 4.1.5 on 2023-01-25 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_place_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='restaurant', serialize=False, to='accounts.place'),
        ),
    ]