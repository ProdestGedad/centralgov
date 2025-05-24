from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ueciaudit.views import DashboardView

urlpatterns = [

    # dashboard “home” (opcional)
    path('auditoria/', DashboardView.as_view(), name='ueciaudit:dashboard'),

    # rota de logout que o header espera
    path('logout/', auth_views.LogoutView.as_view(next_page='auditoria/'), name='logout_view'),


    path('admin/', admin.site.urls),
    path('auditoria/', include('ueciaudit.urls', namespace='ueciaudit')),
]
