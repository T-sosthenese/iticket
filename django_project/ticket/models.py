from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CHOICES = (
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Resolved', 'Resolved'),
)


class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='engineer')
    ticket_id = models.CharField(max_length=15, unique=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    status = models.CharField(max_length=20, choices=CHOICES, default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    severity = models.CharField(max_length=5, choices=(('A', 'A'), ('B', 'B')), default='B')
    contact_mode = models.CharField(max_length=20, choices=(('Phone', 'Phone'), ('Email', 'Email')))
    is_assigned_to_engineer = models.BooleanField(default=False)