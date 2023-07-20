from django.contrib import admin
from tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'status','user']
    list_filter = ['user']
    search_fields = ['title', 'user__username','text']

admin.site.register(Ticket, TicketAdmin)
