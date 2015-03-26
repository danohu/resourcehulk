from django_pg import models
from datetime import datetime
import uuid

def random_id(*args, **kwargs):
    return uuid.uuid4().hex

class SourceInfo(models.Model):
    '''
    Contains source information
    '''
    id = models.AutoField(primary_key=True)
    contributor = models.CharField(max_length=200)
    license = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    info = models.JSONField(type=dict, default={})

class Search(models.Model):
    '''
    Represents one run of any of the data-searching code
    '''
    label = models.CharField(max_length=10, primary_key=True)
    metadata = models.JSONField(type=dict)
    source = models.ForeignKey('SourceInfo', null=True,blank=True)

    def __str__(self):
        return self.label or '<untitled>'


class SearchResult(models.Model):
    id = models.AutoField(primary_key=True)
    search = models.ForeignKey('Search', related_name='results')
    sequencenum = models.IntegerField()
    metadata = models.JSONField(type=dict)

    def __str__(self):
        return self.metadata.get('extract', str(self.sequencenum))


class Commodity(models.Model):
    commodity_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    commodity_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'commodity_table'

    def __str__(self):
        return self.commodity_name or '<untitled>'


class CompanyAlias(models.Model):
    company_alias = models.CharField(primary_key=True, max_length=200, default=random_id)
    company_id = models.CharField(max_length=200)

    class Meta:
        db_table = 'company_alias_table'

    def __str__(self):
        return self.company_alias or '<untitled>'



class Company(models.Model):
    company_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    open_lei_id = models.CharField(max_length=200, blank=True)
    duns_number = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200)
    ticker_symbol = models.CharField(max_length=200, blank=True)
    tax_id = models.CharField(max_length=200, blank=True)
    open_corp_id = models.CharField(max_length=200, blank=True)
    vat_id = models.CharField(max_length=200, blank=True)
    company_url = models.CharField(max_length=200, blank=True)
    
    cik = models.IntegerField(blank=True, null=True, db_index=True)
    sic = models.IntegerField(blank=True, null=True)
    jurisdiction = models.CharField(max_length=50, blank=True)

    source=models.ForeignKey('SourceInfo', blank=True,null=True, related_name='companies')

    class Meta:
        db_table = 'company_table'

    def __str__(self):
        return self.company_name or '<untitled>'


class ConcessionAlias(models.Model):
    concession_alias = models.CharField(primary_key=True, max_length=200)
    concession_id = models.CharField(max_length=200)

    class Meta:
        db_table = 'concession_alias_table'

    def __str__(self):
        return self.concession_alias or '<untitled>'


class Concession(models.Model):
    concession_id = models.CharField(primary_key=True, max_length=200)
    concession_name = models.CharField(max_length=200)
    unep_geo_id = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200)
    source = models.ForeignKey('SourceInfo', null=True,blank=True)

    class Meta:
        db_table = 'concession_table'

    def __str__(self):
        return self.concession_name or '<untitled>'



class Contract(models.Model):
    contract_id = models.CharField(primary_key=True, max_length=200)
    doc = models.ForeignKey('Document',null=True,blank=True)
    country = models.CharField(max_length=200)
    sign_date = models.CharField(max_length=200)
    title_type = models.CharField(max_length=200, blank=True)
    source_url = models.CharField(max_length=200)
    doc_cloud_id = models.CharField(max_length=200)
    doc_cloud_url = models.CharField(max_length=200)
    sign_year = models.CharField(max_length=200)
    source = models.ForeignKey('SourceInfo', null=True,blank=True)

    class Meta:
        db_table = 'contract_table'

    def __str__(self):
        return self.contract_id or '<untitled>'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class Document(models.Model):
    doc_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    host_url = models.CharField(max_length=200, default='')
    source_url = models.CharField(max_length=200, default='')
    source = models.ForeignKey('SourceInfo', null=True,blank=True)

    class Meta:
        db_table = 'document_table'

    def __str__(self):
        return self.host_url or '<untitled>'

class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    project_name = models.CharField(max_length=200,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    source = models.ForeignKey('SourceInfo', null=True,blank=True)

    class Meta:
        db_table = 'project_table'


    def __str__(self):
        return self.project_name or '<untitled>'


class Statement(models.Model):
    statement_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    doc = models.ForeignKey(Document,blank=True,null=True,default=None)
    statement_content = models.CharField(max_length=200)
    definitive = models.BooleanField(default=False)

    projects = models.ManyToManyField('Project', db_table='project_link_table', blank=True)
    companies = models.ManyToManyField('Company', db_table='company_link_table', blank=True)
    concessions = models.ManyToManyField('Concession', db_table='concession_link_table',
                                         blank=True)
    contracts = models.ManyToManyField('Contract', db_table='contract_link_table',
                                      blank=True)

    source = models.ForeignKey('SourceInfo', null=True,blank=True)


    class Meta:
        db_table = 'statement_table'

    def __str__(self):
        return self.statement_content or '<untitled>'
