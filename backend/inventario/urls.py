from rest_framework import routers
from .views import ProductoViewSet

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = router.urls
