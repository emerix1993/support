from tickets.models import Ticket
from django.contrib.auth import get_user_model

user = get_user_model()


def manager_takes(user, ticket):
    ticket.manager = user
    ticket.save()
    return ticket
