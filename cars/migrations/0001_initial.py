# Generated by Django 4.2.5 on 2023-10-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body', models.CharField(max_length=10)),
                ('engine_volume', models.FloatField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
