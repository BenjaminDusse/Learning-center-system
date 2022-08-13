# Generated by Django 3.2.13 on 2022-08-11 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_branch_center'),
        ('finance', '0002_transaction_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='branch.branch'),
            preserve_default=False,
        ),
    ]