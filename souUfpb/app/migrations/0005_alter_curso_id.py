# Generated by Django 4.2.6 on 2023-10-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_relacaodisciplinas_periodo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
