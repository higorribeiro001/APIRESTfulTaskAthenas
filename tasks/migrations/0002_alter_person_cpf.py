# Generated by Django 5.1.1 on 2024-09-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
