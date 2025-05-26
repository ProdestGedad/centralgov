# ueciaudit/urls.py

from django.urls import path
from .views import (
    DashboardView,
    NormaListView, NormaCreateView, NormaUpdateView, NormaDeleteView,
    ProcedimentoListView, ProcedimentoCreateView, ProcedimentoUpdateView, ProcedimentoDeleteView,
    AuditoriaListView, AuditoriaCreateView, AuditoriaUpdateView, AuditoriaDeleteView,
    ChecklistItemListView, ChecklistItemCreateView, ChecklistItemUpdateView, ChecklistItemDeleteView,
    NaoConformidadeListView, NaoConformidadeCreateView, NaoConformidadeUpdateView, NaoConformidadeDeleteView,
    ManualAuditoriaView,
)

app_name = 'ueciaudit'

urlpatterns = [
    # Dashboard inicial
    path('', DashboardView.as_view(), name='dashboard'),

    # Normas
    path('normas/', NormaListView.as_view(), name='norma_list'),
    path('normas/nova/', NormaCreateView.as_view(), name='norma_create'),
    path('normas/<int:pk>/editar/', NormaUpdateView.as_view(), name='norma_update'),
    path('normas/<int:pk>/deletar/', NormaDeleteView.as_view(), name='norma_delete'),

    # Procedimentos
    path('procedimentos/', ProcedimentoListView.as_view(), name='procedimento_list'),
    path('procedimentos/novo/', ProcedimentoCreateView.as_view(), name='procedimento_create'),
    path('procedimentos/<int:pk>/editar/', ProcedimentoUpdateView.as_view(), name='procedimento_update'),
    path('procedimentos/<int:pk>/deletar/', ProcedimentoDeleteView.as_view(), name='procedimento_delete'),

    # Auditorias
    path('auditorias/', AuditoriaListView.as_view(), name='auditoria_list'),
    path('auditorias/nova/', AuditoriaCreateView.as_view(), name='auditoria_create'),
    path('auditorias/<int:pk>/editar/', AuditoriaUpdateView.as_view(), name='auditoria_update'),
    path('auditorias/<int:pk>/deletar/', AuditoriaDeleteView.as_view(), name='auditoria_delete'),

    # Check-Lists
    path('checklistitens/', ChecklistItemListView.as_view(), name='checklistitem_list'),
    path('checklistitens/novo/', ChecklistItemCreateView.as_view(), name='checklistitem_create'),
    path('checklistitens/<int:pk>/editar/', ChecklistItemUpdateView.as_view(), name='checklistitem_update'),
    path('checklistitens/<int:pk>/deletar/', ChecklistItemDeleteView.as_view(), name='checklistitem_delete'),

    # Não-Conformidades
    path('naoconformidades/', NaoConformidadeListView.as_view(), name='naoconformidade_list'),
    path('naoconformidades/nova/', NaoConformidadeCreateView.as_view(), name='naoconformidade_create'),
    path('naoconformidades/<int:pk>/editar/', NaoConformidadeUpdateView.as_view(), name='naoconformidade_update'),
    path('naoconformidades/<int:pk>/deletar/', NaoConformidadeDeleteView.as_view(), name='naoconformidade_delete'),

    # Manual de Auditoria
    path('manual/', ManualAuditoriaView.as_view(), name='manual'),
]
