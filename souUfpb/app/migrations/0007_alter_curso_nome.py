# Generated by Django 4.2.6 on 2023-10-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_curso_chminima_alter_relacaodisciplinas_periodo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="nome",
            field=models.CharField(max_length=128),
        ),
    ]
