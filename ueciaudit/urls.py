from django.urls import path
from . import views

app_name = 'ueciaudit'


urlpatterns = [

# —— Dashboard inicial —————————————————————————————
    path('', views.DashboardView.as_view(), name='dashboard'),

    # ——— Norma —————————————————————————————————————
    path('normas/', views.NormaListView.as_view(), name='norma_list'),
    path('normas/nova/', views.NormaCreateView.as_view(), name='norma_create'),
    path('normas/<int:pk>/editar/', views.NormaUpdateView.as_view(), name='norma_update'),
    path('normas/<int:pk>/deletar/', views.NormaDeleteView.as_view(), name='norma_delete'),

    # ——— Procedimento —————————————————————————————————
    path('procedimentos/', views.ProcedimentoListView.as_view(), name='procedimento_list'),
    path('procedimentos/novo/', views.ProcedimentoCreateView.as_view(), name='procedimento_create'),
    path('procedimentos/<int:pk>/editar/', views.ProcedimentoUpdateView.as_view(), name='procedimento_update'),
    path('procedimentos/<int:pk>/deletar/', views.ProcedimentoDeleteView.as_view(), name='procedimento_delete'),

    # ——— Auditoria ———————————————————————————————————
    path('auditorias/', views.AuditoriaListView.as_view(), name='auditoria_list'),
    path('auditorias/nova/', views.AuditoriaCreateView.as_view(), name='auditoria_create'),
    path('auditorias/<int:pk>/editar/', views.AuditoriaUpdateView.as_view(), name='auditoria_update'),
    path('auditorias/<int:pk>/deletar/', views.AuditoriaDeleteView.as_view(), name='auditoria_delete'),

    # ——— ChecklistItem ————————————————————————————————
    path('checklistitens/', views.ChecklistItemListView.as_view(), name='checklistitem_list'),
    path('checklistitens/novo/', views.ChecklistItemCreateView.as_view(), name='checklistitem_create'),
    path('checklistitens/<int:pk>/editar/', views.ChecklistItemUpdateView.as_view(), name='checklistitem_update'),
    path('checklistitens/<int:pk>/deletar/', views.ChecklistItemDeleteView.as_view(), name='checklistitem_delete'),

    # ——— Não-Conformidade —————————————————————————————
    path('naoconformidades/', views.NaoConformidadeListView.as_view(), name='naoconformidade_list'),
    path('naoconformidades/nova/', views.NaoConformidadeCreateView.as_view(), name='naoconformidade_create'),
    path('naoconformidades/<int:pk>/editar/', views.NaoConformidadeUpdateView.as_view(), name='naoconformidade_update'),
    path('naoconformidades/<int:pk>/deletar/', views.NaoConformidadeDeleteView.as_view(), name='naoconformidade_delete'),
]
