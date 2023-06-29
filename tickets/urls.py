from django.urls import path
from tickets.api import TicketAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("",TicketAPIViewSet,basename="tickets")
urlpatterns = router.urls