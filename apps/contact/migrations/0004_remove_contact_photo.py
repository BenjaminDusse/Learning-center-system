# Generated by Django 3.2.13 on 2022-08-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_rename_author_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='photo',
        ),
    ]