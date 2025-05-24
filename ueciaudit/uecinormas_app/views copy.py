from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator

from main.genericviews import DeferResolveUrl, GenericDataTable, GenericEditv2, GenericRecordView
from main.minio import MinioRelatedModelFiles
from main.permissions import check_roles

from .forms import NormaForm, UploadPDFForm
from .models import Norma

ADMINS_DO_MODULO = set(["UECI", "Admin"])


class NormaLView(GenericDataTable):
    TITLE = "Normas da UECI"
    DESCRIPTION = "Listagem de Normas da UECI"
    QUERYSET = Norma.objects.all()
    LABELS = {
        "titulo": "Título",
        "tema": "Tema",
        "emitente": "Emitente",
        "aprovacao": "Aprovacao",
        "vigencia": "Vigencia",
    }
    FORMATS = {}
    FORMAT_DICTS = {}
    HEADING_STYLES = {
        "titulo": {"width": "30%", "max-width": "300px"},
        "tema": {"width": "45%", "max-width": "450px"},
        "emitente": {"width": "5%", "max-width": "90px"},
        "aprovacao": {"width": "5%", "max-width": "90px"},
        "vigencia": {"width": "5%", "max-width": "90px"},
        None: {"width": "10%"},
    }
    DATA_STYLES = {
        "titulo": {"text-overflow": "ellipsis", "overflow": "hidden", "white-space": "nowrap", "width": "30%", "max-width": "300px"},
        "tema": {"text-overflow": "ellipsis", "overflow": "hidden", "white-space": "nowrap", "width": "45%", "max-width": "450px"},
        "emitente": {"text-overflow": "ellipsis", "overflow": "hidden", "white-space": "nowrap", "width": "5%", "max-width": "90px"},
        "aprovacao": {"text-overflow": "ellipsis", "overflow": "hidden", "white-space": "nowrap", "width": "5%", "max-width": "90px"},
        "vigencia": {"text-overflow": "ellipsis", "overflow": "hidden", "white-space": "nowrap", "width": "5%", "max-width": "90px"},
        None: {"text-align": "center", "padding": "0px !important"},
    }
    LOAD_ALSO = []
    CREATELINK = DeferResolveUrl("ueci_norma_criar")
    CREATEWHAT = "Norma"
    URL_DETAIL = "ueci_norma_detalhe"
    URL_EDIT = "ueci_norma_editar"
    URL_DELETE = "ueci_norma_editar"
    ACTION_TEMPLATE = "uecinormas/ueci_norma_actions.html"
    OBJECT_MODE = True
    RESPONSIVE = False

    def _can_create(self, roles: list[str] = []) -> bool:
        return len(ADMINS_DO_MODULO.intersection(roles)) > 0

    def _can_edit(self, roles: list[str] = []) -> bool:
        return len(ADMINS_DO_MODULO.intersection(roles)) > 0

    def _can_delete(self, roles: list[str] = []) -> bool:
        return len(ADMINS_DO_MODULO.intersection(roles)) > 0


class NormaRView(GenericRecordView):
    TITLE = "Norma"
    DECRIPTION = "Detalhes da Norma"
    MODEL = Norma
    LABELS = {
        "titulo": "Título da Norma",
        "tema": "Tema da Norma",
        "emitente": "Emitente",
        "sistema": "Sistema",
        "codigo": "Código da Norma",
        "versao": "Versão",
        "aprovacao": "Aprovação",
        "vigencia": "Vigência",
    }
    SUBPAGES_PRE = "uecinormas/ueci_norma_file.html"


@method_decorator(check_roles(*ADMINS_DO_MODULO), name="dispatch")
class NormaCUDView(GenericEditv2):
    PARENTMODEL = None
    PARENTFIELD = ""
    MODEL = Norma
    FORM = NormaForm
    URL_SELF_KEY = "ueci_norma_detalhe"
    URL_PARENT_KEY = "ueci_norma_listar"

    def _perform_deletion(self, instance: Norma) -> None:
        mfs = MinioRelatedModelFiles(instance)
        arq = next(iter(mfs.list_path()), None)
        if arq is not None:
            mfs.delete_path(arq)
            arq = None
        return super()._perform_deletion(instance)


@check_roles(*ADMINS_DO_MODULO)
def upload_pdf(request: HttpRequest, pk: int) -> HttpResponse:
    norma = get_object_or_404(Norma, pk=pk)
    mfs = MinioRelatedModelFiles(norma)
    arq = next(iter(mfs.list_path()), None)
    if request.method == "POST":
        form = UploadPDFForm(request.POST, request.FILES)
        if arq is not None:
            mfs.delete_path(arq)
            arq = None
        if form.is_valid():
            file = form.cleaned_data["pdf"]
            if file is not None:
                mfs.write_uploadedfile(file)
            return redirect("listar_normas")
    else:
        form = UploadPDFForm()
    return render(request, "uecinormas/upload_pdf.html", {"form": form, "norma": norma, "arq": (arq or "").rsplit("/", 1)[-1]})
