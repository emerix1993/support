from rest_framework import serializers
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ticket
        fields = ["id", "title", "text", "visibility", "status", "user"]
        read_only_fields = ["visibility", "status"]

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def validate(self, attrs):
        return attrs