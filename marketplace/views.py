
from rest_framework import viewsets
from .models import Producto, Cliente, Pedido, DetallePedido
from .serializers import ProductoSerializer, ClienteSerializer, PedidoSerializer, DetallePedidoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
# Vistas basadas en clases
class ProductoListView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
# Vista de API para el modelo Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@api_view(['GET'])
def lista_productos_personalizada(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detalle_producto_personalizado(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

# Vista de API para el modelo Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


@api_view(['GET'])
def lista_clientes_personalizada(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detalle_cliente_personalizado(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)


# Vista de API para el modelo Pedido
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

@api_view(['GET'])
def lista_pedidos_personalizada(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detalle_pedido_personalizado(request, pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

# Vista de API para el modelo DetallePedido
class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


@api_view(['GET'])
def lista_detalles_pedido_personalizada(request):
    if request.method == 'GET':
        detalles_pedido = DetallePedido.objects.all()
        serializer = DetallePedidoSerializer(detalles_pedido, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detalle_detalle_pedido_personalizado(request, pk):
    try:
        detalle_pedido = DetallePedido.objects.get(pk=pk)
    except DetallePedido.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DetallePedidoSerializer(detalle_pedido)
        return Response(serializer.data)
