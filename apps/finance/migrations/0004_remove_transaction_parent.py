# Generated by Django 3.2.13 on 2022-08-13 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_transaction_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='parent',
        ),
    ]
