# Generated by Django 3.2.13 on 2022-08-08 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('student_number', models.CharField(max_length=7, unique=True)),
                ('status', models.CharField(choices=[('Studying', 'Studying'), ('Not Studying', 'Not Studying')], default='Studying', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('teacher_number', models.CharField(max_length=7)),
                ('status', models.CharField(choices=[('Working', 'Working'), ('Not Working', 'Not Working')], default='Working', max_length=50)),
                ('saldo', models.DecimalField(decimal_places=3, help_text='load and salary', max_digits=9)),
                ('learning_center', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_center', to='center.center')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
