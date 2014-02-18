from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader, RequestContext
from models import Vehicle

def index(request):
    all_vehicles_list = Vehicle.objects.order_by('-year')[:5]
    template = loader.get_template('inventory_tracker/index.html')
    context = RequestContext(request, {
            'all_vehicles_list': all_vehicles_list,
            })
    return HttpResponse(template.render(context))

def detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'inventory_tracker/detail.html', {
            'vehicle': vehicle})
