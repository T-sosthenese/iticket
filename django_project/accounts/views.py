from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import RegisterCustomerForm

User = get_user_model()

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.username = var.email
            var.save()
            messages.success(request, 'Account created. You can proceed to login.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Check the form errors')
            return redirect('register-customer')
    else:
        form = RegisterCustomerForm()
        context = {'form':form}
        return render(request, 'accounts/register_customer.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Check for form errors.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Your session has been terminated. Login again to continue')
    return redirect('login')

# Change Password - in application
# Update profile