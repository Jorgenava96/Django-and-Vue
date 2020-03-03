from rest_framework import routers

from .viewsets import ExpedienteViewSet

router = routers.SimpleRouter()
router.register('Expediente', ExpedienteViewSet)

urlpatterns = router.urls