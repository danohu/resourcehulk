'''
import some json output
'''

from django.core.management.base import BaseCommand
from optparse import make_option
from hulk import models
import uuid
import json
import re
from canopener import canopener


def edgar_link(_fn):
    #fn = '111270610-K_2010-09-28_0001062993-10-003164.txt_extracted_4.txt'
    groups = _fn.strip('"').split('/')
    cik = groups[-2]
    exhibit_num = re.search('(\d+).txt$', groups[-1]).group(1)
    filenum = re.search('_([\d\-]+).txt_extracted_', groups[-1]).group(1)
    filenum_short = ''.join(filenum.split('-'))
    url = 'http://www.sec.gov/Archives/edgar/data/%s/%s/%s-index.htm' % (cik, filenum_short, filenum)
    human_exhibit_num = str(int(exhibit_num) + 1) # don't make users count from 0
    return _fn.strip(), url, human_exhibit_num

class Command(BaseCommand):
    args = 'loadsearch --label MYLABEL <path>'
    option_list = BaseCommand.option_list + (
        make_option('--label', dest="label", default=None),)

    def postprocess_line(self, jline, kwargs):
        if ('edgar' in jline['filepath']):
            ignored, jline['edgar_link'], jline['edgar_exhibit_number'] = edgar_link(jline['filepath'])
        import pdb; pdb.set_trace()
        return jline

    def handle(self, path, **kwargs):
        label = kwargs['label'] or uuid.uuid4().hex[:10]
        search = models.Search(label, metadata={})
        search.save()
        fh = canopener(path)
        for linenum, line in enumerate(fh,1):
            js = json.loads(line)
            js = self.postprocess_line(js, kwargs)
            result = models.SearchResult(
                sequencenum = linenum,
                search= search,
                metadata=js)
            result.save()
        print('output at http://localhost:8000/search/%s' % search.label)

