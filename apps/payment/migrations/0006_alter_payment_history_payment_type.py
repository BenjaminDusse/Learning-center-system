# Generated by Django 3.2.13 on 2022-08-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20220810_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_history',
            name='payment_type',
            field=models.CharField(choices=[('Naqd', 'Cash'), ('Plastik kartochka', 'Plastic Card'), ("Pul o'tkazish", 'Money Transfer')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]