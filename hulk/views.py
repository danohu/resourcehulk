from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    # show the result
    per_page = 2000
    srch = get_object_or_404(models.Search, pk=search_id)
    paginator = Paginator(srch.results.all(), per_page)
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return render_to_response('search.jinja',
                              {'results': results,
                               'search': srch,
                               'keys': [
                                   ('filepath', 'Full document (copy)'),
                                   ('source_url', 'Full document (original)'),
                                   ('company_name', 'Company'),
                                   ('filing_type', 'Type of filing'),
                                   ('filing_date', 'Date filed'),
                                   #('cik', 'CIK (Edgar company identifier)'),
                                   ('edgar_exhibit_number', 'Exhibition number (on EDGAR)'),
                                   #('score', 'Number of matches in document'),
                                   ('extract', 'Start of document'),
                                   ('positives', 'Matches in context'),
                                   ('country_names', 'Countries named in document')],

                           })
    
