from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.status import HTTP_403_FORBIDDEN
from users.roles import Role
from tickets import services as ticket_services
from tickets.models import Ticket, Message
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from tickets.serializers import TicketSerializer, TicketAssignSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from tickets.permissons import RoleIsAdmin, RoleIsUser, RoleIsManager, IsOwner
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


class TicketAPIViewSet(ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        all_tickets = Ticket.objects.all()
        print(user.role)
        print(all_tickets)
        if user.role == Role.ADMIN:
            return all_tickets
        elif user.role == Role.MANAGER:
            return all_tickets.filter(Q(manager=user) | Q(manager=None))
        else:
            return all_tickets.filter(Q(user=user))


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
        elif self.action == "reassign":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


    @action(detail=True, methods=["PATCH"])
    def take(self, request, pk=None):
        ticket = self.get_object()
        return Response("Ok")
        # user = self.request.user
        # if user.role != Role.MANAGER:
        #     raise PermissionDenied("You don't have rights", 403)
        serializer = TicketAssignSerializer(data={"ticket_id": request.user.id})
        serializer.is_valid()
        ticket = serializer.assign(ticket,User)
        # return Response(TicketSerializer(ticket).data)



    @action(detail=True, methods=["PUT"])
    def reassign(self, request, pk=None):
        ticket = self.get_object()
        user = request.user
        if user.role != Role.ADMIN:
            raise PermissionDenied("You don't have rights", code=HTTP_403_FORBIDDEN)
        new_manager_id = request.data.get("new_manager_id")

        serializer = TicketAssignSerializer(data={"manager_id": new_manager_id})
        serializer.is_valid()
        ticket = serializer.assign(ticket,user)

        return Response(TicketSerializer(ticket).data)


class MessageListCreateAPIView(ListCreateAPIView):
    serializer_class = MessageSerializer
    lookup_field = "ticket_id"

    def get_queryset(self):
        return Message.objects.filter(
            Q(ticket__user=self.request.user) | Q(ticket__manager=self.request.user),
            ticket_id=self.kwargs[self.lookup_field],)

    @staticmethod
    def get_ticket(user, ticket_id) -> Ticket:
        tickets = Ticket.objects.filter(Q(user=user) | Q(manager=user))
        return get_object_or_404(tickets, id=ticket_id)

    def post(self, request, ticket_id: int):
        ticket = self.get_ticket(request.user, ticket_id)
        payload = {"text": request.data["text"],"ticket": ticket_id,}
        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# class MessageListCreateAPIView(ListCreateAPIView):
#     serializer_class = MessageSerializer
#     lookup_field = ["ticket_id"]
#     lookup_field_kwarg = ["ticket_id"]
#
# def post(self, request, ticket_id):
#     ticket = self.get_ticket(request.user, ticket_id)
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     self.perform_create(serializer)
#     headers = self.get_success_headers(serializer.data)
#     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TicketDeleteAPIView(CreateAPIView):
    pass


class TicketUpdateAPIView(CreateAPIView):
    pass


class TicketListAPIView(CreateAPIView):
    pass


class TicketRetrieveAPIView(CreateAPIView):
    pass
