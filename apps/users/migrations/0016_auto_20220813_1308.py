# Generated by Django 3.2.13 on 2022-08-13 08:08

import birthday.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth_dayofyear_internal',
            field=models.PositiveSmallIntegerField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=birthday.fields.BirthdayField(blank=True, null=True),
        ),
    ]
