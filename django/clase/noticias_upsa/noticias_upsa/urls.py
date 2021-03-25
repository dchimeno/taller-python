"""noticias_upsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from noticias.views import listado_comentarios, ComentarioDetailView
from noticias.api import comentarios, ComentarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comentarios/', listado_comentarios, name="listado-comentarios"),
    path('comentarios/<int:pk>/', ComentarioDetailView.as_view(), name="detalle-comentario"),
    path('api/comentarios/', comentarios, name="api-listado-comentarios"),
    path('api/comentarios/<int:pk>/', ComentarioView.as_view(), name="api-detalle-comentario"),
    path('api/', include("rest_framework.urls", namespace="rest_framework"))
]
