from django import forms
from .models import Ticket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'ticket_title',
            'ticket_description',
            'contact_mode'
        ]

class AssignTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['engineer']