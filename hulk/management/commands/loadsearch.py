'''
import some json output
'''

from django.core.management.base import BaseCommand
from optparse import make_option
from hulk import models
import uuid
import json




class Command(BaseCommand):
    args = 'loadsearch --label MYLABEL <path>'
    option_list = BaseCommand.option_list + (
        make_option('--label', dest="label", default=None),)

    def handle(self, path, **kwargs):
        label = kwargs['label'] or uuid.uuid4().hex[:10]
        search = models.Search(label, metadata={})
        search.save()
        fh = open(path, 'r')
        for linenum, line in enumerate(fh,1):
            js = json.loads(line)
            result = models.SearchResult(
                sequencenum = linenum,
                search= search,
                metadata=js)
            result.save()

