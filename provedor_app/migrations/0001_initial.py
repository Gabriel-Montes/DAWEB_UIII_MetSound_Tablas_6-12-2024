# Generated by Django 5.1.3 on 2024-12-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id_prove', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('fecha_entre', models.DateField()),
                ('telefono', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=50)),
            ],
        ),
    ]
