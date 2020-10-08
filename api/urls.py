from django.urls import path, include
from api.api_views import ProductoListR, ProductoDetalleR
from rest_framework.routers import DefaultRouter

from api.api_views import (
        ProductoList,
        ProductoDetalle,
        CategoriaSave,
        CategoriaList,
        SubCategoriaList,
        CategoriaDetalle,
        SubCategoriaAdd,
        ProductoViewSet,
        UserCreate,
        LoginView
    )

router = DefaultRouter()
router.register('v3/productos', ProductoViewSet, basename='productos3')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),

    # path refactorizacion serializers
    path('v2/productos/', ProductoListR.as_view(), name='producto_list_r'),
    path('v2/productos/<int:pk>', ProductoDetalleR.as_view(), name='producto_detalle_r'),

    path('v2/categorias/', CategoriaList.as_view(), name='categoria_list'),
    path('v2/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_detalle'),

    #path('v2/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_list'),
    path('v2/categorias/<int:pk>/subcategorias', SubCategoriaList.as_view(), name='categoria_detalle'),

    path('v2/categorias_save/', CategoriaSave.as_view(), name='categoria_save'),

    path('v2/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(), name='add_sub'),

    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear'),

    path("v4/login/", LoginView.as_view(), name="login")
]

urlpatterns += router.urls