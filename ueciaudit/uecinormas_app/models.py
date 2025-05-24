from django.db import models

from main.minio import SingleFileModelMixin


class Norma(models.Model, SingleFileModelMixin):
    CATEGORIA_CHOICES = [
        ("GERAL", "Geral"),
        ("EXCLUSIVA", "Exclusiva"),
    ]

    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    anexo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    atualizacao = models.DateField(blank=True, null=True)
    versao = models.CharField(max_length=20, blank=True, null=True)
    aprovacao = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    vigencia = models.DateField(blank=True, null=True)
    publicacao_dio = models.DateField(blank=True, null=True)
    errata = models.DateField(blank=True, null=True)
    processo = models.CharField(max_length=100, blank=True, null=True)
    edocs = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    revogada_dio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome or "Norma sem nome"

    @property
    def pdf(self):
        return self.file

    @property
    def pdf_name(self):
        return self.file_name
