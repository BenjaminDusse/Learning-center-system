# Generated by Django 3.2.13 on 2022-08-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_online',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_activity',
        ),
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('student', 'student'), ('teacher', 'teacher'), ('staff', 'staff')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='saldo',
            field=models.IntegerField(blank=True, help_text='loan and salary', null=True),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
