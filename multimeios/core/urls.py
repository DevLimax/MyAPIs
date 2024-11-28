"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Minha API",
      default_version='v1',
      description="Descrição da minha API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@meuapp.com"),
      license=openapi.License(name="Licença do Meu App"),
   ),
   public=True,
)

urlpatterns = [
    path('', include('multimeios.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)