from rest_framework import serializers
from tickets.models import Ticket, Message


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

    def validate_manager_id(self, manager_id):
        return manager_id

    def assign(self, ticket):
        ticket.manager_id = self.validated_data["manager_id"]
        ticket.save()
        return ticket

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["user", "ticket", "timestamp"]

    def validate(self, attrs):
        raise NotImplementedError("You should implement this method")
