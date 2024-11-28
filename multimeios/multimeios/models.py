from django.db import models

class Usuarios(models.Model):
    nome_usuario = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=200)
    matricula = models.IntegerField(unique=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome_usuario
    
class Generos(models.Model):
    genero = models.CharField(max_length=200)
    
    def __str__(self):
        return self.genero
    
class Livros(models.Model):
    titulo = models.CharField(max_length=200,null=False)
    autor = models.CharField(max_length=200,null=True)
    genero_1 = models.ForeignKey(Generos, on_delete=models.CASCADE,null=False,related_name="livros_genero_1")
    genero_2 = models.ForeignKey(Generos, on_delete=models.CASCADE,null=True,related_name="livros_genero_2")
    is_rented = models.BooleanField(default=False)
    image = models.ImageField(upload_to="image/",blank=True,null=False)
    
    def __str__(self):
        return self.titulo
    