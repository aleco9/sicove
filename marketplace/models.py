from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    # Validación  Precio no puede ser negativo
    def validate_precio_no_negativo(self):
        if self.precio < 0:
            raise ValidationError("El precio no puede ser negativo.")

    # Validación  Descripción debe tener al menos 10 caracteres
    def validate_descripcion_longitud(self):
        if len(self.descripcion) < 10:
            raise ValidationError("La descripción debe tener al menos 10 caracteres.")

    # Validación  Nombre no puede contener ciertas palabras prohibidas
    def validate_nombre_prohibido(self):
        palabras_prohibidas = ["spam", "spam2", "spam3"]
        for palabra in palabras_prohibidas:
            if palabra in self.nombre.lower():
                raise ValidationError("El nombre contiene una palabra prohibida: {}".format(palabra))


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    # Validación El correo electrónico debe ser válido
    def validate_email_valido(self):
        email_validator = EmailValidator()
        try:
            email_validator(self.email)
        except ValidationError as e:
            raise ValidationError("El correo electrónico no es válido: {}".format(e))

    # Validación El nombre no puede contener caracteres especiales
    def validate_nombre_sin_caracteres_especiales(self):
        if not self.nombre.isalnum():
            raise ValidationError("El nombre no puede contener caracteres especiales.")

    # Validación  El número de teléfono debe tener un formato específico
    def validate_telefono_formato(self):
        # Agrega tu lógica de validación de formato de teléfono aquí
        # Por ejemplo, asegurarse de que el formato sea "(123) 456-7890"
        pass



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    # Validación  El total debe ser mayor que cero
    def validate_total_mayor_que_cero(self):
        if self.total <= 0:
            raise ValidationError("El total debe ser mayor que cero.")

    # Validación El cliente debe tener un correo electrónico
    def validate_cliente_con_email(self):
        if not self.cliente.email:
            raise ValidationError("El cliente debe tener un correo electrónico.")

    # Validación  La fecha de pedido no puede estar en el futuro
    def validate_fecha_pedido_no_futuro(self):
        from django.utils import timezone
        if self.fecha_pedido > timezone.now():
            raise ValidationError("La fecha de pedido no puede estar en el futuro.")


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    # Validación  La cantidad debe ser al menos 1
    def validate_cantidad_minima(self):
        if self.cantidad < 1:
            raise ValidationError("La cantidad debe ser al menos 1.")

    # Validación El producto debe estar disponible
    def validate_producto_disponible(self):
        if self.cantidad > self.producto.stock:
            raise ValidationError("El producto no está disponible en la cantidad solicitada.")

    # Validación El producto no puede estar en la misma categoría que otro producto en el pedido
    def validate_producto_misma_categoria(self):
        otros_productos_en_pedido = DetallePedido.objects.filter(pedido=self.pedido).exclude(id=self.id)
        for otro_producto in otros_productos_en_pedido:
            if self.producto.categoria == otro_producto.producto.categoria:
                raise ValidationError("El producto no puede estar en la misma categoría que otro producto en el pedido.")