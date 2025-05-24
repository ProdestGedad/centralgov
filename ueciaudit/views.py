from django.urls import reverse_lazy
from django.views import generic
from .models import (
    Norma, Procedimento, Auditoria,
    ChecklistItem, NaoConformidade
)
from .forms import (
    NormaForm, ProcedimentoForm, AuditoriaForm,
    ChecklistItemForm, NaoConformidadeForm
)

class PageMixin:
    page_title       = None
    page_description = ''
    breadcrumb       = []  # lista de tuplas: (rótulo, url_name, *args)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title']       = self.page_title
        ctx['description'] = self.page_description
        # monta breadcrumbs, sempre incluindo o próprio título no fim
        crumbs = list(self.breadcrumb)
        crumbs.append((self.page_title,))
        ctx['breadcrumbs'] = crumbs
        return ctx

class DashboardView(PageMixin, generic.TemplateView):
    template_name    = 'ueciaudit/dashboard.html'
    page_title       = 'Gestão de Auditorias de Normas e Procedimentos'
    page_description = 'Visão geral rápida de todas as seções'
    breadcrumb       = [('Início', 'ueciaudit:dashboard')]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['ultimas_normas']        = Norma.objects.order_by('-criado_em')[:5]
        ctx['ultimos_procedimentos'] = Procedimento.objects.order_by('-criado_em')[:5]
        ctx['ultimas_auditorias']    = Auditoria.objects.order_by('-data_agendada')[:5]
        ctx['ultimos_itens']         = ChecklistItem.objects.order_by('-id')[:5]
        ctx['ultimas_ncs']           = NaoConformidade.objects.order_by('-id')[:5]
        return ctx

# ——— Normas ——————————————————————————————————————————————
class NormaListView(PageMixin, generic.ListView):
    model               = Norma
    template_name       = 'ueciaudit/norma_list.html'
    context_object_name = 'normas'
    page_title          = 'Normas'
    page_description    = 'Listagem de todas as normas'
    breadcrumb          = [('Início', 'ueciaudit:dashboard')]

class NormaCreateView(PageMixin, generic.CreateView):
    model         = Norma
    form_class    = NormaForm
    template_name = 'ueciaudit/norma_form.html'
    success_url   = reverse_lazy('ueciaudit:norma_list')
    page_title       = 'Nova Norma'
    page_description = 'Cadastre uma nova norma'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Normas', 'ueciaudit:norma_list'),
    ]

class NormaUpdateView(PageMixin, generic.UpdateView):
    model         = Norma
    form_class    = NormaForm
    template_name = 'ueciaudit/norma_form.html'
    success_url   = reverse_lazy('ueciaudit:norma_list')
    page_title       = 'Editar Norma'
    page_description = 'Atualize os dados da norma'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Normas', 'ueciaudit:norma_list'),
    ]

class NormaDeleteView(PageMixin, generic.DeleteView):
    model         = Norma
    template_name = 'ueciaudit/norma_confirm_delete.html'
    success_url   = reverse_lazy('ueciaudit:norma_list')
    page_title       = 'Excluir Norma'
    page_description = 'Confirme a exclusão da norma'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Normas', 'ueciaudit:norma_list'),
    ]

# ——— Procedimentos ————————————————————————————————————————
class ProcedimentoListView(PageMixin, generic.ListView):
    model               = Procedimento
    template_name       = 'ueciaudit/procedimento_list.html'
    context_object_name = 'procedimentos'
    page_title          = 'Procedimentos'
    page_description    = 'Listagem de procedimentos vinculados a normas'
    breadcrumb          = [('Início', 'ueciaudit:dashboard')]

class ProcedimentoCreateView(PageMixin, generic.CreateView):
    model         = Procedimento
    form_class    = ProcedimentoForm
    template_name = 'ueciaudit/procedimento_form.html'
    success_url   = reverse_lazy('ueciaudit:procedimento_list')
    page_title       = 'Novo Procedimento'
    page_description = 'Cadastre um novo procedimento'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Procedimentos', 'ueciaudit:procedimento_list'),
    ]

class ProcedimentoUpdateView(PageMixin, generic.UpdateView):
    model         = Procedimento
    form_class    = ProcedimentoForm
    template_name = 'ueciaudit/procedimento_form.html'
    success_url   = reverse_lazy('ueciaudit:procedimento_list')
    page_title       = 'Editar Procedimento'
    page_description = 'Atualize os dados do procedimento'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Procedimentos', 'ueciaudit:procedimento_list'),
    ]

class ProcedimentoDeleteView(PageMixin, generic.DeleteView):
    model         = Procedimento
    template_name = 'ueciaudit/procedimento_confirm_delete.html'
    success_url   = reverse_lazy('ueciaudit:procedimento_list')
    page_title       = 'Excluir Procedimento'
    page_description = 'Confirme a exclusão do procedimento'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Procedimentos', 'ueciaudit:procedimento_list'),
    ]

# ——— Auditorias ——————————————————————————————————————————
class AuditoriaListView(PageMixin, generic.ListView):
    model               = Auditoria
    template_name       = 'ueciaudit/auditoria_list.html'
    context_object_name = 'auditorias'
    page_title          = 'Auditorias'
    page_description    = 'Listagem de auditorias agendadas'
    breadcrumb          = [('Início', 'ueciaudit:dashboard')]

class AuditoriaCreateView(PageMixin, generic.CreateView):
    model         = Auditoria
    form_class    = AuditoriaForm
    template_name = 'ueciaudit/auditoria_form.html'
    success_url   = reverse_lazy('ueciaudit:auditoria_list')
    page_title       = 'Nova Auditoria'
    page_description = 'Agende uma nova auditoria'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Auditorias', 'ueciaudit:auditoria_list'),
    ]

class AuditoriaUpdateView(PageMixin, generic.UpdateView):
    model         = Auditoria
    form_class    = AuditoriaForm
    template_name = 'ueciaudit/auditoria_form.html'
    success_url   = reverse_lazy('ueciaudit:auditoria_list')
    page_title       = 'Editar Auditoria'
    page_description = 'Atualize os dados da auditoria'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Auditorias', 'ueciaudit:auditoria_list'),
    ]

class AuditoriaDeleteView(PageMixin, generic.DeleteView):
    model         = Auditoria
    template_name = 'ueciaudit/auditoria_confirm_delete.html'
    success_url   = reverse_lazy('ueciaudit:auditoria_list')
    page_title       = 'Excluir Auditoria'
    page_description = 'Confirme a exclusão da auditoria'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Auditorias', 'ueciaudit:auditoria_list'),
    ]

# ——— ChecklistItem ———————————————————————————————————————
class ChecklistItemListView(PageMixin, generic.ListView):
    model               = ChecklistItem
    template_name       = 'ueciaudit/checklistitem_list.html'
    context_object_name = 'itens'
    page_title          = 'Itens de Checklist'
    page_description    = 'Verifique cada item de auditoria'
    breadcrumb          = [('Início', 'ueciaudit:dashboard')]

class ChecklistItemCreateView(PageMixin, generic.CreateView):
    model         = ChecklistItem
    form_class    = ChecklistItemForm
    template_name = 'ueciaudit/checklistitem_form.html'
    success_url   = reverse_lazy('ueciaudit:checklistitem_list')
    page_title       = 'Novo Item de Checklist'
    page_description = 'Adicione um novo item ao checklist'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Itens de Checklist', 'ueciaudit:checklistitem_list'),
    ]

class ChecklistItemUpdateView(PageMixin, generic.UpdateView):
    model         = ChecklistItem
    form_class    = ChecklistItemForm
    template_name = 'ueciaudit/checklistitem_form.html'
    success_url   = reverse_lazy('ueciaudit:checklistitem_list')
    page_title       = 'Editar Item de Checklist'
    page_description = 'Atualize o item de checklist'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Itens de Checklist', 'ueciaudit:checklistitem_list'),
    ]

class ChecklistItemDeleteView(PageMixin, generic.DeleteView):
    model         = ChecklistItem
    template_name = 'ueciaudit/checklistitem_confirm_delete.html'
    success_url   = reverse_lazy('ueciaudit:checklistitem_list')
    page_title       = 'Excluir Item de Checklist'
    page_description = 'Confirme a exclusão do item'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Itens de Checklist', 'ueciaudit:checklistitem_list'),
    ]

# ——— Não-Conformidade —————————————————————————————————————
class NaoConformidadeListView(PageMixin, generic.ListView):
    model               = NaoConformidade
    template_name       = 'ueciaudit/naoconformidade_list.html'
    context_object_name = 'ncs'
    page_title          = 'Não-Conformidades'
    page_description    = 'Registro de não-conformidades'
    breadcrumb          = [('Início', 'ueciaudit:dashboard')]

class NaoConformidadeCreateView(PageMixin, generic.CreateView):
    model         = NaoConformidade
    form_class    = NaoConformidadeForm
    template_name = 'ueciaudit/naoconformidade_form.html'
    success_url   = reverse_lazy('ueciaudit:naoconformidade_list')
    page_title       = 'Nova Não-Conformidade'
    page_description = 'Registre uma nova não-conformidade'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Não-Conformidades', 'ueciaudit:naoconformidade_list'),
    ]

class NaoConformidadeUpdateView(PageMixin, generic.UpdateView):
    model         = NaoConformidade
    form_class    = NaoConformidadeForm
    template_name = 'ueciaudit/naoconformidade_form.html'
    success_url   = reverse_lazy('ueciaudit:naoconformidade_list')
    page_title       = 'Editar Não-Conformidade'
    page_description = 'Atualize a não-conformidade'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Não-Conformidades', 'ueciaudit:naoconformidade_list'),
    ]

class NaoConformidadeDeleteView(PageMixin, generic.DeleteView):
    model         = NaoConformidade
    template_name = 'ueciaudit/naoconformidade_confirm_delete.html'
    success_url   = reverse_lazy('ueciaudit:naoconformidade_list')
    page_title       = 'Excluir Não-Conformidade'
    page_description = 'Confirme a exclusão da não-conformidade'
    breadcrumb       = [
        ('Início', 'ueciaudit:dashboard'),
        ('Não-Conformidades', 'ueciaudit:naoconformidade_list'),
    ]
