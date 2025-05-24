from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Norma(models.Model):
    titulo        = models.CharField(max_length=200)
    versao        = models.CharField(max_length=20)
    descricao     = models.TextField()
    data_vigencia = models.DateField()
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} v{self.versao}"

class Procedimento(models.Model):
    norma       = models.ForeignKey(Norma, on_delete=models.CASCADE, related_name='procedimentos')
    titulo      = models.CharField(max_length=200)
    descricao   = models.TextField()
    documentos  = models.FileField(upload_to='procedimentos/', blank=True, null=True)
    criado_em   = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Auditoria(models.Model):
    procedimento   = models.ForeignKey(Procedimento, on_delete=models.PROTECT)
    data_agendada  = models.DateField()
    iniciado_em    = models.DateTimeField(null=True, blank=True)
    finalizado_em  = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = [('A','Agendada'),('E','Em andamento'),('C','Concluída')]
    status         = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    equipe         = models.ManyToManyField(User, related_name='auditorias')

    def __str__(self):
        return f"Auditoria {self.pk} ({self.get_status_display()})"

class ChecklistItem(models.Model):
    auditoria    = models.ForeignKey(Auditoria, on_delete=models.CASCADE, related_name='itens')
    descricao    = models.TextField()
    obrigatorio  = models.BooleanField(default=True)
    RESULTADO    = [('C','Conforme'),('N','Não conforme'),('I','N/A')]
    resultado    = models.CharField(max_length=1, choices=RESULTADO, blank=True)
    evidencia    = models.FileField(upload_to='evidencias/', blank=True, null=True)
    comentarios  = models.TextField(blank=True)

    def __str__(self):
        return f"Item {self.pk} - {self.get_resultado_display() or 'Pendente'}"

class NaoConformidade(models.Model):
    item                 = models.ForeignKey(ChecklistItem, on_delete=models.CASCADE, related_name='naos')
    severidade           = models.CharField(max_length=1, choices=[('B','Baixa'),('M','Média'),('A','Alta')])
    descricao            = models.TextField()
    corrigido            = models.BooleanField(default=False)
    data_correcao        = models.DateField(null=True, blank=True)
    responsavel_correcao = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"NC {self.pk} ({self.get_severidade_display()})"

class AuditLog(models.Model):
    OPER  = [('C','Criou'),('U','Atualizou'),('D','Deletou')]
    operacao   = models.CharField(max_length=1, choices=OPER)
    usuario    = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    modelo     = models.CharField(max_length=50)
    objeto_id  = models.PositiveIntegerField()
    detalhes   = models.JSONField(blank=True, null=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_operacao_display()} {self.modelo}[{self.objeto_id}]"
