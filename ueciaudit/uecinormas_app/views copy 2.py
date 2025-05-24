from django.shortcuts import get_object_or_404, redirect, render

from .forms import NormaForm, UploadPDFForm  # ← novo form importado
from .models import Norma


def upload_pdf(request, pk):
    norma = get_object_or_404(Norma, pk=pk)
    if request.method == "POST":
        form = UploadPDFForm(request.POST, request.FILES, instance=norma)
        if form.is_valid():
            form.save()
            return redirect("listar_normas")
    else:
        form = UploadPDFForm(instance=norma)
    return render(request, "uecinormas/upload_pdf.html", {"form": form, "norma": norma})


def listar_normas(request):
    normas = Norma.objects.all().order_by("-vigencia")
    return render(request, "uecinormas/listar.html", {"normas": normas})


def cadastrar_norma(request):
    if request.method == "POST":
        form = NormaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listar_normas")
    else:
        form = NormaForm()
    return render(request, "uecinormas/cadastrar.html", {"form": form})


def editar_norma(request, pk):
    norma = get_object_or_404(Norma, pk=pk)
    if request.method == "POST":
        form = NormaForm(request.POST, request.FILES, instance=norma)
        if form.is_valid():
            form.save()
            return redirect("listar_normas")
    else:
        form = NormaForm(instance=norma)
    return render(request, "uecinormas/cadastrar.html", {"form": form, "editar": True})


def excluir_norma(request, pk):
    norma = get_object_or_404(Norma, pk=pk)
    if request.method == "POST":
        norma.delete()
        return redirect("listar_normas")
    return render(request, "uecinormas/confirmar_exclusao.html", {"norma": norma})
