# Generated by Django 4.2.6 on 2023-10-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_curso_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relacaodisciplinas",
            name="periodo",
            field=models.CharField(max_length=32),
        ),
    ]
