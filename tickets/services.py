from tickets.models import Ticket
from django.contrib.auth import get_user_model

User = get_user_model()


def manager_takes(User, ticket):
    ticket.manager = User
    ticket.save()
    return ticket
