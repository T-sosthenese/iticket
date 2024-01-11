from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
import random
import string

from .forms import CreateTicketForm, AssignTicketForm
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
                    messages.success(request, 'Your ticket has been submitted. A support engineer will reach out soon.')
                    return redirect('customer-active-tickets')
                except IntegrityError:
                    continue
        else:
            messages.warning(request, 'Something went wrong. Check your form input again')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm
        context = {'form':form}
        return render(request, 'ticket/create_ticket.html', context)

# Show all active tickets that have been created
def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_active_tickets.html', context)

# Show all resolved tickets
def customer_resolved_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_resolved_tickets.html', context)

# Assign ticket to engineers
def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_assigned_to_engineer = True
            var.save()
            messages.success(request, 'Ticket has been assigned to {}'.format(var.engineer))
            return redirect('ticket-queue')
        else:
            messages.warning(request, 'Something went wrong. Check form data')
            return redirect('assign-ticket') # Revisiting this later
    else:
        form = AssignTicketForm()
        context = {'form':form}
        return render(request, 'ticket/assign_ticket.html', context)

# Ticket details
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    context = {'ticket':ticket}
    return render(request, 'ticket/ticket_details.html', context)

# Ticket queue (for only admins)
def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigned_to_engineer=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/ticket_queue.html', context)