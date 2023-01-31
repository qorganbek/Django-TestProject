# Generated by Django 4.1.5 on 2023-01-25 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_passport_person_alter_subject_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.AlterField(
            model_name='passport',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='passports', to='accounts.person'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
