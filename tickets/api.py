from tickets.models import Ticket
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from tickets.serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated


class TicketAPIViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


class TicketDeleteAPIView(CreateAPIView):
    pass


class TicketUpdateAPIView(CreateAPIView):
    pass


class TicketListAPIView(CreateAPIView):
    pass


class TicketRetrieveAPIView(CreateAPIView):
    pass
