# marketplace/admin.py

from django.contrib import admin
from .models import Producto, Cliente, Pedido, DetallePedido

# Modelo administrativo personalizado para el modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion')
    list_filter = ('nombre', 'precio')
    search_fields = ('nombre', 'descripcion')

# Modelo administrativo personalizado para el modelo Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    list_filter = ('nombre', 'email')
    search_fields = ('nombre', 'email')

# Modelo administrativo personalizado para el modelo Pedido
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_pedido', 'total')
    list_filter = ('cliente', 'fecha_pedido')
    search_fields = ('cliente__nombre',)

# Modelo administrativo personalizado para el modelo DetallePedido
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')
    list_filter = ('pedido', 'producto')
    search_fields = ('pedido__cliente__nombre', 'producto__nombre')

# Registra los modelos en el panel de administración
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)
