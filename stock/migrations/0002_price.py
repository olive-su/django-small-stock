# Generated by Django 4.0.1 on 2022-02-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=40, null=True)),
                ('date', models.DateField()),
                ('open', models.BigIntegerField(null=True)),
                ('high', models.BigIntegerField(null=True)),
                ('low', models.BigIntegerField(null=True)),
                ('close', models.BigIntegerField(null=True)),
                ('diff', models.BigIntegerField(null=True)),
                ('volume', models.BigIntegerField(null=True)),
            ],
        ),
    ]
