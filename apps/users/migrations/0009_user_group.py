# Generated by Django 3.2.13 on 2022-08-10 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220810_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to='users.usergroup'),
            preserve_default=False,
        ),
    ]
