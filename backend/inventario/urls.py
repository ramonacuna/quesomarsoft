from rest_framework import routers
from .views import ProductoViewSet,ExistenciaViewSet

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'existencias', ExistenciaViewSet)

urlpatterns = router.urls
