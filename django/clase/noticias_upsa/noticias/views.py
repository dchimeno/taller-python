import os
from django.shortcuts import render
from django.views.generic import DetailView
from noticias.models import Comentario, Noticia


def listado_comentarios(request):
    context = {
        "object_list": Comentario.objects.all()
    }

    return render(request, os.path.join("noticias", "comentario_list.html"), context=context)


class ComentarioDetailView(DetailView):
    model = Comentario

