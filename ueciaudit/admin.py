from django.contrib import admin
from .models import (
    Norma, Procedimento, Auditoria,
    ChecklistItem, NaoConformidade, AuditLog
)

@admin.register(Norma)
class NormaAdmin(admin.ModelAdmin):
    list_display  = ('titulo','versao','data_vigencia')
    search_fields = ('titulo','versao')

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display  = ('titulo','norma')
    list_filter   = ('norma',)

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display  = ('procedimento','data_agendada','status')
    list_filter   = ('status',)

@admin.register(ChecklistItem)
class ChecklistItemAdmin(admin.ModelAdmin):
    list_display  = ('auditoria','obrigatorio','resultado')

@admin.register(NaoConformidade)
class NCAdmin(admin.ModelAdmin):
    list_display  = ('item','severidade','corrigido')
    list_filter   = ('severidade','corrigido')

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display    = ('operacao','modelo','objeto_id','usuario','timestamp')
    readonly_fields = ('operacao','modelo','objeto_id','usuario','detalhes','timestamp')
