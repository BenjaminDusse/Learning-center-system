# Generated by Django 3.2.13 on 2022-08-10 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20220810_1421'),
        ('users', '0003_auto_20220810_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='contact.contact'),
        ),
    ]
