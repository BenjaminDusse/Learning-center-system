# Generated by Django 3.2.13 on 2022-08-10 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='hide_transaction',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='level',
        ),
        migrations.AddField(
            model_name='contact',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]
