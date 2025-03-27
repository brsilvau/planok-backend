from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet, UnidadPropiedadViewSet, ClienteViewSet

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'unidades', UnidadPropiedadViewSet)



urlpatterns = router.urls
