# Generated by Django 3.2.13 on 2022-08-10 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='show_password',
        ),
    ]
