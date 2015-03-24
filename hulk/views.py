from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from hulk import models
# Create your views here.

def index(request):
    return HttpResponse('Not Implemented')

def company(request, company_id):
    company = get_object_or_404(models.Company, pk=company_id)
    return HttpResponse('company %s ' % company.name)

def project(request, project_id):
    project = get_object_or_404(models.Project, pk=project_id)
    return HttpResponse('project %s ' % project.name)

def search(request, search_id):
    srch = get_object_or_404(models.search, pk=search_id)
    pass
    
