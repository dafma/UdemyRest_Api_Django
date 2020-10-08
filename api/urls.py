from django.urls import path, include
from api.api_views import ProductoListR, ProductoDetalleR
from api.api_views import (
        ProductoList,
        ProductoDetalle,
        CategoriaSave,
        CategoriaList,
        SubCategoriaList,
    )

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),

    # path refactorizacion serializers
    path('v2/productos/', ProductoListR.as_view(), name='producto_list_r'),
    path('v2/productos/<int:pk>', ProductoDetalleR.as_view(), name='producto_detalle_r'),

    path('v2/categorias/', CategoriaList.as_view(), name='categoria_list'),
    path('v2/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_list'),

    path('v2/categorias_save/', CategoriaSave.as_view(), name='categoria_save'),

]
