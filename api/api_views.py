from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# otra forma
from rest_framework import generics, viewsets, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto, Categoria, SubCategoria
from .serializers import (
    ProductoSerializer,
    CategoriaSerializer,
    SubCategoriaSerializer,
    UserSerializer
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


class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class SubCategoriaList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset

    serializer_class = SubCategoriaSerializer


class SubCategoriaAdd(APIView):
    # sobrescribe el metodo post
    def post(self, request, cat_pk):
        # obtenemos del request el argumento descripcion
        descripcion = request.data.get("descripcion")
        print("descripcion")
        # construimos un string data
        data = {"categoria": cat_pk, "descripcion": descripcion}
        # serializamos la data
        serializer = SubCategoriaSerializer(data=data)
        # si la data ha sido serializada correctamente
        if serializer.is_valid():
            # guardamos la data
            subcat = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # si no creamos un data bad request
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer