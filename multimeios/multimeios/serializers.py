from rest_framework import serializers
from .models import Usuarios,Generos,Livros

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = "__all__"
        

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Generos
        fields= "__all__"
        
class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Livros
        fields = "__all__"