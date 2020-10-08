from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Categoria


def categoria_list(request):
    max_objects = 20
    cat = Categoria.objects.all()[:max_objects]
    data = {"results": list(cat.values("descripcion", "activo"))}
    return JsonResponse(data)


def categoria_detalle(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    data = {
        "results": {
            "desciption": cat.descripcion,
            "activo": cat.activo
        }
    }
    return JsonResponse(data)
# Create your views here.
