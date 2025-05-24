from django.urls import path

from . import views

urlpatterns = [
    path("uecinormas/", views.NormaLView.as_view(), name="ueci_norma_listar"),  # List
    path("uecinormas/<int:pk>/detalhe/", views.NormaRView.as_view(), name="ueci_norma_detalhe"),  # Read
    path("uecinormas/-/criar/", views.NormaCUDView.as_view(new=True), name="ueci_norma_criar"),  # Create
    path("uecinormas/<int:pk>/editar/", views.NormaCUDView.as_view(new=False), name="ueci_norma_editar"),  # Update+Delete
    path("uecinormas/<int:pk>/upload-pdf/", views.upload_pdf, name="ueci_norma_uploadpdf"),  # Upload PDF
    #     path("uecinormas/", views.listar_normas, name="listar_normas"),
    #     path("uecinormas/nova/", views.cadastrar_norma, name="cadastrar_norma"),
    #     path("uecinormas/editar/<int:pk>/", views.editar_norma, name="editar_norma"),
    #     path("uecinormas/<int:pk>/upload-pdf/", views.upload_pdf, name="upload_pdf"),
]
