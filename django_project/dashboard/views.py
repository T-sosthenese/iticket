from django.shortcuts import render

def dashboard(request):
    if request.user.is_customer:
        return render(request, 'dashboard/customer_dashboard.html')