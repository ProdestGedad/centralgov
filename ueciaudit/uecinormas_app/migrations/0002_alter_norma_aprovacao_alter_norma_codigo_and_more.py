# Generated by Django 5.0.14 on 2025-05-14 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("uecinormas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="norma",
            name="aprovacao",
            field=models.CharField(blank=True, default="", max_length=80),
        ),
        migrations.AlterField(
            model_name="norma",
            name="codigo",
            field=models.CharField(blank=True, default="", max_length=254),
        ),
        migrations.AlterField(
            model_name="norma",
            name="emitente",
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name="norma",
            name="instrucao_servico",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="norma",
            name="sistema",
            field=models.CharField(blank=True, default="", max_length=254),
        ),
        migrations.AlterField(
            model_name="norma",
            name="tema",
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name="norma",
            name="titulo",
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name="norma",
            name="versao",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
