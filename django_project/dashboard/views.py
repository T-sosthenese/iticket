from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    if request.user.is_customer:
        return render(request, 'dashboard/customer_dashboard.html')