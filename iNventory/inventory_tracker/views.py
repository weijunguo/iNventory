from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader, RequestContext
from models import SalesPerson, Vehicle

def index(request):
    all_objects = Vehicle.objects.all()
    template = loader.get_template('inventory_tracker/index.html')
    context = RequestContext(request, {
            'all_objects': all_objects,
            })
    return HttpResponse(template.render(context))
