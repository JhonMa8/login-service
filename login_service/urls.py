from django.contrib import admin
from django.urls import path, include
from accounts.views import login_page  # Asegúrate que esta vista existe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login_page'),  # 👈 Esta línea arregla el error
    path('api/auth/', include('accounts.urls')),
]

