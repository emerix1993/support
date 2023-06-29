# Generated by Django 4.2.2 on 2023-06-28 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='manager_tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='messages', to='tickets.ticket'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
