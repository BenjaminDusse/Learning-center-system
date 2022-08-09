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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_center', to='center.center')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
