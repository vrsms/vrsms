# Generated by Django 3.2.5 on 2022-06-02 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=30, verbose_name='Reference')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTicket',
            fields=[
                ('ref_no', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('approval_status', models.BooleanField(default=False, verbose_name='Is It Approved ?')),
                ('item_serviced', models.CharField(max_length=30)),
                ('frequency', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
            options={
                'verbose_name': 'Service Ticket',
                'verbose_name_plural': 'Service Tickets',
                'ordering': ('ref_no', 'title', 'driver', 'vehicle', 'approval_status', 'item_serviced', 'frequency', 'cost', 'date'),
                'permissions': [('change_service_ticket_status', 'Can change the status of service tickets'), ('close_service_ticket', 'Can remove a service ticket by setting its status as closed')],
            },
        ),
    ]
