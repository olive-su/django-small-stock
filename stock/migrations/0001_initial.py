# Generated by Django 4.0.1 on 2022-01-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=40)),
                ('last_update', models.DateField()),
            ],
        ),
    ]