from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UsuariosView,GenerosView,LivrosView

router = DefaultRouter()
router.register('Usuarios', UsuariosView, basename="Usuarios")
router.register('Generos', GenerosView, basename="Generos")
router.register('Livros', LivrosView, basename="Livros")

urlpatterns = router.urls