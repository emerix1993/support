from django.urls import path
from tickets.api import TicketAPIViewSet, MessageListCreateAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TicketAPIViewSet, basename="tickets")
urlpatterns = router.urls + [path("<int:ticket_id>/messages/", MessageListCreateAPIView.as_view())]
