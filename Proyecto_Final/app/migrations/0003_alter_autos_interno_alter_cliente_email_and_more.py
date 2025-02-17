# Generated by Django 4.2 on 2025-01-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_alquiler_interno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos',
            name='interno',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
    ]
