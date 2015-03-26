'''
import some json output
'''

from django.core.management.base import BaseCommand
from optparse import make_option
from hulk import models
import hulk.utils
import uuid
import json
import re
import sys
from canopener import canopener


def edgar_link(_fn):
    # deprecated
    groups = _fn.strip('"').split('/')
    cik = groups[-2]
    exhibit_num = re.search('(\d+).txt$', groups[-1]).group(1)
    filenum = re.search('_([\d\-]+).txt_extracted_', groups[-1]).group(1)
    filenum_short = ''.join(filenum.split('-'))
    url = 'http://www.sec.gov/Archives/edgar/data/%s/%s/%s-index.htm' % (cik, filenum_short, filenum)
    human_exhibit_num = str(int(exhibit_num) + 1) # don't make users count from 0
    return _fn.strip(), url, human_exhibit_num, cik

def decompose_edgar(fn):
    #fn = '111270610-K_2010-09-28_0001062993-10-003164.txt_extracted_4.txt'
    parts = {}
    groups = fn.strip('"').split('/')
    parts['cik'] = groups[-2]
    assert parts['cik'].isdigit()
    exhibit_num = re.search('(\d+).txt$', groups[-1]).group(1)
    filenum = re.search('_([\d\-]+).txt_extracted_', groups[-1]).group(1)
    filenum_short = ''.join(filenum.split('-'))
    parts['source_url'] = 'http://www.sec.gov/Archives/edgar/data/%s/%s/%s-index.htm' % (parts['cik'], filenum_short, filenum)
    parts['edgar_exhibit_number'] = str(int(exhibit_num) + 1) # don't make users count from 0
    filename_segments = groups[-1].split('_')
    parts['filing_type'] = filename_segments[0]
    parts['filing_date'] = filename_segments[1]
    return parts
    
class Command(BaseCommand):
    args = 'loadsearch --label MYLABEL <path>'
    option_list = BaseCommand.option_list + (
        make_option('--label', dest="label", default=None),)

    def postprocess_line(self, jline, kwargs):
        if ('edgar' in jline['filepath']):
            parts = decompose_edgar(jline['filepath'])
            for label in (
                    'edgar_exhibit_number',
                    'source_url',
                    'cik',
                    'filing_date',
                    'filing_type',
                    ):
                jline[label] = parts[label]
        comp = models.Company.objects.get(cik=jline['cik'])
        jline['company_name'] = comp.company_name
        return jline

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

        label = kwargs['label'] or uuid.uuid4().hex[:10]
        search = models.Search(
            label,
            metadata={},
            source=sourceinfo)
        search.save()
        fh = canopener(path)
        for linenum, line in enumerate(fh,1):
            js = json.loads(line)
            try:
                js = self.postprocess_line(js, kwargs)
            except AssertionError:
                continue
            result = models.SearchResult(
                sequencenum = linenum,
                search= search,
                metadata=js)
            result.save()
        print('output at http://localhost:8000/search/%s' % search.label)

