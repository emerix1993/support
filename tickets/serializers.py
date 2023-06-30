from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ticket
        fields = ["id", "title", "text", "visibility", "status", "user","manager"]
        read_only_fields = ["visibility", "status","manager"]

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def validate(self, attrs):
        return attrs

class TicketAssignSerializer(serializers.Serializer):
    manager_id = serializers.IntegerField()

    def assign(self, ticket):
        ticket.manager_id = self.validated_data["manager_id"]
        ticket.save()
        return ticket
