from django.urls import path
from .views import login_view, registrar_usuario, login_page, lista_usuarios

urlpatterns = [
    path('login/', login_view),
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('', login_page, name='login_page'),
    path('users/', lista_usuarios),
]

