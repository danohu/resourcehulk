from django.core.management.base import BaseCommand, CommandError
from hulk import models
import csv
import os

def tullow2013():
    fn = os.path.dirname(__file__) + '/../../../data/20150312_tullow_cr2013.csv'
    reader = csv.reader(open(fn))
    next(reader)
    for line in reader:
        project, country, company, year, source, link = line
        company, created = models.Company.objects.get_or_create(
            company_name = company,
            defaults = {}
            )
        project, created = models.Project.objects.get_or_create(
            project_name = project,
            defaults = {}
            )
        document, created = models.Document.objects.get_or_create(
            host_url = link)
        print('document - created %s' % created)
        statement, created = models.Statement.objects.get_or_create(
            defaults = {'definitive': False},
            statement_content = 'Listing in Tullow annual report -- %s, %s' % (project, country),
            doc=document,
            )
        statement.companies.add(company)
        statement.projects.add(project)

def exxonreport():
    fn = os.path.dirname(__file__) + '/../../../data/20150313_exxonmobil_report.csv'
    reader = csv.reader(open(fn))
    next(reader)
    for line in reader:
        basin, project,refterm,stage,country, commodity_type, project_type, company, subsidiary,partner,source_name, source_url, source_page = line
        company, created = models.Company.objects.get_or_create(
            company_name = company,
            defaults = {}
            )
        project, created = models.Project.objects.get_or_create(
            project_name = project,
            defaults = {}
            )
        document, created = models.Document.objects.get_or_create(
            host_url = source_url,
            source_url = source_url)
        print('document - created %s' % created)
        statement, created = models.Statement.objects.get_or_create(
            defaults = {'definitive': False},
            statement_content = 'Listing in %s annual report -- %s' % (company.company_name, project.project_name),
            doc=document,
            )
        statement.companies.add(company)
        statement.projects.add(project)






class Command(BaseCommand):
    args = 'hulkgrab <source> <options>'
    help = 'import data into resourcehulk'
    
    sources = {
        'tullow2013': tullow2013,
        'exxonmobil': exxonreport}
        

    def handle(self, source, *args, **kwargs):
        self.stdout.write('importing data')
        if source == 'all':
            self.graball()
        else:
            self.sources[source]()
        

    def graball(self):
        for (k,v) in self.sources.items():
            v()
