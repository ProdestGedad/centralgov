from django.db import models


class Norma(models.Model):
    titulo = models.CharField(max_length=254, default="A definir")
    tema = models.CharField(max_length=254, default="A definir")
    emitente = models.CharField(max_length=254, default="A definir")
    sistema = models.CharField(max_length=254, default="A definir")
    codigo = models.CharField(max_length=254, default="A definir")
    versao = models.IntegerField()
    aprovacao = models.CharField(max_length=80, default="A definir")
    instrucao_servico = models.CharField(max_length=20, default="A definir")
    vigencia = models.DateField(blank=True, null=True)
    pdf = models.FileField(upload_to="normas_pdfs/", blank=True, null=True)

    def __str__(self):
        return self.titulo
