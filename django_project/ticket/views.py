from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
import random
import string

from .forms import CreateTicketForm
from .models import Ticket

# Creating a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            while not var.ticket_id:
                id = ''.join(random.choices(string.digits, k=6))
                try:
                    var.ticket_id = id
                    var.save()
                    break
                except IntegrityError:
                    continue
            messages.success(request, 'Your ticket has been submitted. A support engineer will reach out soon.')
            return redirect('customer-tickets')
        else:
            messages.warning(request, 'Something went wrong. Check your form input again')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm
        context = {'form':form}
        return render(request, 'ticket/create_ticket.html', context)

# Show all tickets that have been created
def customer_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user)
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_tickets.html', context)

# Assign ticket to engineers
def assign_ticket(request):
    pass

# Ticket details
# Ticket queue (for only admins)