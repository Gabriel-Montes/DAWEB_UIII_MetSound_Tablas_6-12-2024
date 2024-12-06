# Generated by Django 5.1.3 on 2024-12-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id_instru', models.IntegerField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('tamano', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
                ('mantenimiento', models.DateField()),
                ('vendido', models.CharField(max_length=2)),
            ],
        ),
    ]
