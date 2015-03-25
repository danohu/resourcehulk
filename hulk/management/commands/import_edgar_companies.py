'''
Import basic information on companies from edgar

'''

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = 'loadsea --label MYLABEL <path>'
    
