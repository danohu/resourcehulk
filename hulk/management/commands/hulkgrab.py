from django.core.management.base import BaseCommand, CommandError
from hulk import models
import csv
import os

def tullow2013():
    fn = os.path.dirname(__file__) + '/../../../data/20150312_tullow_cr2013.csv'
    print(fn)
    reader = csv.reader(open(fn))
    next(reader)
    company, created = models.Company.objects.g_or_create(
        defaults = 
        )
    for line in reader:
        project, country, company, year, source, link = line
        document, created = models.Document.objects.get_or_create(
            title = source,
            source_url = link)
        print('document - created %s' % created)
        statement, created = models.Statement.objects.get_or_create(
            defaults = {'confidence': 0},
            name = 'Listing in Tullow annual report -- %s, %s' % (project, country),
            document=document,
            )
        statement.add_company(company)




class Command(BaseCommand):
    args = 'hulkgrab <source> <options>'
    help = 'import data into resourcehulk'
    
    sources = {
        'tullow2013': tullow2013}
        

    def handle(self, source, *args, **kwargs):
        self.stdout.write('importing data')
        if source == 'all':
            self.graball()
        else:
            self.sources[source]()
        

    def graball(self):
        for (k,v) in self.sources.items():
            v()
