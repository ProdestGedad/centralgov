from django.db import models


class Norma(models.Model):
    titulo = models.CharField(max_length=254)  # obrigatório
    tema = models.CharField(max_length=254)  # obrigatório
    emitente = models.CharField(max_length=254)  # obrigatório
    sistema = models.CharField(max_length=254, blank=True, default="")
    codigo = models.CharField(max_length=254, blank=True, default="")
    versao = models.IntegerField(blank=True, null=True)
    aprovacao = models.CharField(max_length=80, blank=True, default="")
    # instrucao_servico = models.CharField(max_length=20, blank=True, default='')
    # vigencia = models.DateField(blank=True, null=True)
    vigencia = models.CharField(max_length=50, blank=True, default="")

    def __str__(self):
        return self.titulo
