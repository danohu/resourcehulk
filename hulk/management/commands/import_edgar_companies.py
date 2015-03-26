'''
Import basic information on companies from edgar
'''

from django.core.management.base import BaseCommand
import csv
from hulk import models
import hulk.utils
from canopener import canopener
import sys

class Command(BaseCommand):
    args = 'import_edgar_companies <filename>'
    help = '''
      import basic company info from EDGAR
      files you probably want to use this on:
      s3://sec-edgar.openoil.net/oil/companies_by_sic_oil.txt
      s3://sec-edgar.openoil.net/mining/companies_by_sic.txt
    '''

    def handle(self, path, **kwargs):
        sourceinfo = models.SourceInfo(
            contributor='OpenOil',
            license='CC-BY-SA-4.0',
            info={
                'description': 'Import of company information from EDGAR',
                'source_file':  path,
                'code_version': hulk.utils.get_git_revision(),
                'command_run': ' '.join(sys.argv)
                })
        sourceinfo.save()
        fh = canopener(path)
        reader = csv.reader(fh, delimiter='\t')
        for line in reader:
            (cik, name, state, sic) = line
            jurisdiction = 'US_%s' % state
            comp, created = models.Company.objects.get_or_create(
                company_name = name.title(),
                cik = cik,
                jurisdiction = jurisdiction,
                sic = sic,
                source=sourceinfo,
                defaults={})
            comp.save()


    
