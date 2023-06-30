from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from tickets import services as ticket_services
from tickets.models import Ticket
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from tickets.serializers import TicketSerializer,TicketAssignSerializer
from rest_framework.permissions import IsAuthenticated
from tickets.permissons import RoleIsAdmin, RoleIsUser, RoleIsManager, IsOwner


class TicketAPIViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


def get_permissions(self):
    if self.action == "list":
        permission_classes = [RoleIsAdmin | RoleIsManager | RoleIsUser]
    elif self.action == "create":
        permission_classes = [RoleIsUser]
    elif self.action == "retrieve":
        permission_classes = [IsOwner | RoleIsManager | RoleIsAdmin]
    elif self.action == "update":
        permission_classes = [RoleIsManager | RoleIsAdmin]
    elif self.action == "destroy":
        permission_classes = [RoleIsAdmin | RoleIsManager]
    elif self.action == "take":
        permission_classes = [RoleIsManager]
    else:
        permission_classes = []
    return [permission() for permission in permission_classes]


@action(detail=True, methods=["POST"])
def take(self, request, pk=None):
    ticket = self.get_object()
    if ticket.manager:
        raise ValidationError("Ticket is already taken") # ->If a manager is already specified the Permission error
        # is raised (from homework)
    serializer = TicketAssignSerializer(data={"manager_id": request.user.id})
    serializer.assign(ticket)
    return Response(TicketSerializer(ticket).data)



class TicketDeleteAPIView(CreateAPIView):
    pass


class TicketUpdateAPIView(CreateAPIView):
    pass


class TicketListAPIView(CreateAPIView):
    pass


class TicketRetrieveAPIView(CreateAPIView):
    pass
