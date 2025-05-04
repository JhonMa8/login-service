from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'role')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Determinar rol según grupos (o según tu lógica)
        if user.is_superuser:
            role = "admin"
        elif user.groups.filter(name="jefe_brigada").exists():
            role = "jefe_brigada"
        elif user.groups.filter(name="tecnico").exists():
            role = "tecnico"
        elif user.groups.filter(name="botanico").exists():
            role = "botanico"
        else:
            role = ""

        # Incluir token y rol en la respuesta
        data["token"] = data.pop("access")
        data["role"] = role
        return data