from django.shortcuts import render
from .serializers import UsuariosSerializer,GenerosSerializer,LivrosSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Usuarios,Generos,Livros

class UsuariosView(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()
    
    @action(detail=False, methods=['post'])
    def autenticar(self,request):
        email = request.data.get('email')
        senha = request.data.get('senha')
        
        if not email or not senha:
            return Response(
                {"error": "Email e senha são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        usuario = Usuarios.objects.filter(email=email, senha=senha).first()

        if usuario:
            serializer = self.get_serializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        else:
            return Response(
                {"error": "Email ou senha inválidos."},
                status=status.HTTP_401_UNAUTHORIZED
            )   
    
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        matricula = request.data.get('matricula')
        if Usuarios.objects.filter(email=email).exists():
            return Response(
                {
                    "error": "Este e-mail já está em uso.",
                    "status":status.HTTP_400_BAD_REQUEST,
                    "details":email
                },
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if Usuarios.objects.filter(matricula=matricula).exists():
            return Response(
                {
                    "error":"Já existe um Usuario com a matricula informada!",
                    "status":status.HTTP_400_BAD_REQUEST,
                    "details":matricula
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

class LivrosView(viewsets.ModelViewSet):
    serializer_class = LivrosSerializer
    queryset = Livros.objects.all()
    
class GenerosView(viewsets.ModelViewSet):
    serializer_class = GenerosSerializer
    queryset = Generos.objects.all()