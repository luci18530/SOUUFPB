# Generated by Django 4.2.6 on 2023-10-20 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=64)),
                ("numPeriodos", models.IntegerField()),
                ("cargaTotal", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Disciplina",
            fields=[
                (
                    "codigo",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=128)),
                ("carga", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question_text", models.CharField(max_length=200)),
                ("area", models.CharField(default="", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="RelacaoDisciplinas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("periodo", models.IntegerField()),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.curso"
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.disciplina"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Choice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "choice",
                    models.CharField(
                        choices=[
                            ("discordo_totalmente", "1"),
                            ("discordo_parcialmente", "2"),
                            ("neutro", "3"),
                            ("concordo_parcialmente", "4"),
                            ("concordo_totalmente", "5"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.question"
                    ),
                ),
            ],
        ),
    ]