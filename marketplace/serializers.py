
from rest_framework import serializers
from .models import Producto, Cliente, Pedido, DetallePedido

# Serializador para el modelo Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

# Serializador para el modelo Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    # Ejemplo de validación personalizada para el campo 'email'
    def validate_email(self, value):
        # Tu lógica de validación personalizada aquí
        # Por ejemplo, asegurarse de que el correo electrónico sea único
        if Cliente.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este correo electrónico ya está en uso.')
        return value

# Serializador para el modelo Pedido
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

# Serializador para el modelo DetallePedido
class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'
