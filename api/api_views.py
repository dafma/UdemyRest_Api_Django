from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from rest_framework import generics

from .models import Producto, Categoria, SubCategoria
from .serializers import (
        ProductoSerializer,
        CategoriaSerializer,
        SubCategoriaSerializer,
    )


class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()[:20]
        data = ProductoSerializer(prod, many=True).data
        return Response(data)


class ProductoDetalle(APIView):
    def get(self, request, pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductoSerializer(prod).data
        return Response(data)

# SIMPLIFICA CON VISTAS GENERICAS


class ProductoListR(generics.ListCreateAPIView):
    """
    ListCreateAPIView devuelve una lista de entidades o las crea
    tiene operaciones get y post
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetalleR(generics.RetrieveDestroyAPIView):
    """
        RetrieveDestroyAPIView RetrieveDestroyAPIViewrecupera los datos
        de una entidad o los elimina
        permite get o delete
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaSave(generics.CreateAPIView):
    """
        CreateAPIView permite crear entidades pero no las lista
        permite post
    """
    serializer_class = CategoriaSerializer

class SubCategoriaSave(generics.CreateAPIView):
    """
        CreateAPIView permite crear entidades pero no las lista
        permite post
    """
    serializer_class = SubCategoriaSerializer


class CategoriaList(generics.ListCreateAPIView):
    """
    ListCreateAPIView devuelve una lista de entidades o las crea
    tiene operaciones get y post
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class SubCategoriaList(generics.ListCreateAPIView):
    """
    ListCreateAPIView devuelve una lista de entidades o las crea
    tiene operaciones get y post
    """
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer

