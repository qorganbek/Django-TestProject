# Generated by Django 4.1.5 on 2023-01-25 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_subject_student_alter_passport_person_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Passport',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
