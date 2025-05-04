from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect


User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        role = user.role or "no-role"  # ← usa tu campo personalizado
        return Response({
            "token": token.key,
            "role": role
        })
    else:
        return Response(
            {"detail": "Credenciales inválidas"},
            status=status.HTTP_401_UNAUTHORIZED
        )


def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if User.objects.filter(username=username).exists():
            return render(request, 'registrar.html', {'error': 'El usuario ya existe'})

        user = User.objects.create_user(username=username, password=password)
        user.role = role  # ← usa el campo correcto
        user.save()

        return redirect('/')  # vuelve al login
    return render(request, 'registrar.html')

def login_page(request):
    return render(request, 'index.html')