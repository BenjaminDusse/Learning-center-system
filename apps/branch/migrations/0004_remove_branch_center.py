# Generated by Django 3.2.13 on 2022-08-13 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0003_branch_loan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='center',
        ),
    ]
