from rest_framework import routers
from .viewsets import AfiliadoViewSet


router = routers.SimpleRouter()
router.register('remisiones', AfiliadoViewSet)

urlpatterns = router.urls
