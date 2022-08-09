# Generated by Django 3.2.13 on 2022-08-08 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('center', '0001_initial'),
        ('payment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_history',
            name='user',
            field=models.ManyToManyField(related_name='history_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='outcome',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.center'),
        ),
        migrations.AddField(
            model_name='outcome',
            name='payment_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='outcome', to='payment.payment_type'),
        ),
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loan_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='income',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.center'),
        ),
    ]