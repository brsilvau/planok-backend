import uuid
from django.test import TestCase
from django.db import IntegrityError, transaction
from core.models import Cliente, ProyectoInmobiliario, UnidadPropiedad

class ProyectoInmobiliarioModelTest(TestCase):
    def setUp(self):
        self.proyecto = ProyectoInmobiliario.objects.create(
            nombre="Proyecto Test",
            descripcion="Descripción del proyecto",
            ubicacion="Ubicación Test",
            fecha_inicio="2023-01-01",
            fecha_fin="2023-12-31",
            estado="En construccion"
        )

    def test_creacion_proyecto(self):
        """ Se verifica que el proyecto se crea con uuid y con fecha_creacion """
        self.assertIsInstance(self.proyecto, ProyectoInmobiliario)
        self.assertIsInstance(self.proyecto.id, uuid.UUID)
        self.assertIsNotNone(self.proyecto.fecha_creacion)

class ClienteModelTest(TestCase):
    def test_creacion_cliente(self):
        cliente = Cliente.objects.create(
            rut="12345678-9",
            nombre="Juan",
            apellido="Pérez",
            correo_electronico="juan@example.com",
            telefono="123456789"
        )
        """ Se verifica que el cliente se crea con uuid y con fecha_creacion """
        self.assertIsInstance(cliente, Cliente)
        self.assertIsInstance(cliente.id, uuid.UUID)
        self.assertIsNotNone(cliente.fecha_creacion)

    def test_unicidad_campos(self):
        Cliente.objects.create(
            rut="12345678-9",
            nombre="Juan",
            apellido="Pérez",
            correo_electronico="juan@example.com",
            telefono="123456789"
        )
        """ Se verifica que rut y correo no se puede ingresar dos veces """
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Cliente.objects.create(
                    rut="12345678-9",
                    nombre="María",
                    apellido="Gómez",
                    correo_electronico="maria@example.com",
                    telefono="987654321"
                )
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Cliente.objects.create(
                    rut="98765432-1",
                    nombre="Pedro",
                    apellido="López",
                    correo_electronico="juan@example.com",
                    telefono="987654321"
                )

class UnidadPropiedadModelTest(TestCase):
    def setUp(self):
        self.proyecto = ProyectoInmobiliario.objects.create(
            nombre="Proyecto Test",
            descripcion="Descripción del proyecto",
            ubicacion="Ubicación Test",
            fecha_inicio="2023-01-01",
            fecha_fin="2023-12-31",
            estado="En construcción"
        )
        self.cliente = Cliente.objects.create(
            rut="12345678-9",
            nombre="Juan",
            apellido="Pérez",
            correo_electronico="juan@example.com",
            telefono="123456789"
        )

    def test_creacion_unidad_sin_cliente(self):
        unidad = UnidadPropiedad.objects.create(
            numero_unidad="A101",
            tipo_unidad="Departamento",
            metraje_cuadrado=50.5,
            precio_venta=100000.00,
            estado="Disponible",
            proyecto=self.proyecto,
            cliente=None
        )
        """ Se crea correctamente una unidad sin cliente """
        self.assertIsInstance(unidad, UnidadPropiedad)
        self.assertIsNone(unidad.cliente)

    def test_creacion_unidad_con_cliente(self):
        unidad = UnidadPropiedad.objects.create(
            numero_unidad="B202",
            tipo_unidad="Casa",
            metraje_cuadrado=120.75,
            precio_venta=200000.00,
            estado="Vendido",
            proyecto=self.proyecto,
            cliente=self.cliente
        )
        """ Se crea correctamente una unidad con cliente """
        self.assertEqual(unidad.cliente, self.cliente)

    def test_cascade_delete_proyecto(self):
        unidad = UnidadPropiedad.objects.create(
            numero_unidad="C303",
            tipo_unidad="Oficina",
            metraje_cuadrado=80.0,
            precio_venta=150000.00,
            estado="Disponible",
            proyecto=self.proyecto,
            cliente=self.cliente
        )
        proyecto_id = self.proyecto.id
        self.proyecto.delete()
        """ Se eliminan correctamente las unidades al eliminar un proyecto """
        self.assertFalse(UnidadPropiedad.objects.filter(proyecto_id=proyecto_id).exists())

    def test_set_null_cliente_al_eliminar(self):
        unidad = UnidadPropiedad.objects.create(
            numero_unidad="D404",
            tipo_unidad="Departamento",
            metraje_cuadrado=60.0,
            precio_venta=120000.00,
            estado="Reservado",
            proyecto=self.proyecto,
            cliente=self.cliente
        )
        self.cliente.delete()
        unidad.refresh_from_db()
        """ Se elimina la relación unidad-cliente al eliminar el cliente """
        self.assertIsNone(unidad.cliente)
