from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'gas_utilities/service_request_form.html', {'form': form})

class ServiceRequestListView(ListView):
    model = ServiceRequest
    template_name = 'gas_utilities/service_request_list.html'
    context_object_name = 'gas_utilities'
    ordering = ['-submitted_at']

class ServiceRequestDetailView(DetailView):
    model = ServiceRequest
    template_name = 'gas_utilities/service_request_detail.html'
