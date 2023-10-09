"""
URL configuration for sicoveapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from marketplace.views import ProductoViewSet, ClienteViewSet, PedidoViewSet, DetallePedidoViewSet
from marketplace.views  import (
    ProductoListView,
    ProductoDetailView,
    ClienteListView,
    ClienteDetailView,
    lista_productos_personalizada,
    detalle_producto_personalizado,
)


# Crea un enrutador
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detallespedido', DetallePedidoViewSet)
router.register(r'productos', ProductoDetailView, basename='producto')
router.register(r'clientes', ClienteDetailView, basename='cliente')


urlpatterns = [
    # Otras rutas de tu aplicación si las tienes
    path('api/', include(router.urls)),
    
   # Rutas para las vistas basadas en clases (vistas genéricas)
    path('api/productos/', ProductoListView.as_view(), name='producto-list'),
    path('api/productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),

    # Rutas para las vistas personalizadas
    path('api/productos/personalizada/', lista_productos_personalizada, name='producto-list-personalizada'),
    path('api/productos/personalizada/<int:pk>/', detalle_producto_personalizado, name='producto-detail-personalizada'), 
]

