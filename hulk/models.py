from django_pg import models
import uuid

def random_id(*args, **kwargs):
    return uuid.uuid4().hex



"""
class BeneficialOwnership(models.Model):
    owned_by = models.ForeignKey('Company')
    owner_of = models.ForeignKey('Company')

    class Meta:
        managed = False
        db_table = 'benneficial_ownership_table'


class CommodityLink(models.Model):
    commodity = models.ForeignKey('Commodity')
    entity_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'commodity_link_table'

class CompanyLink(models.Model):
    statement = models.ForeignKey('Statement')
    company = models.ForeignKey('Company')

    class Meta:
        managed = False
        db_table = 'company_link_table'


class ConcessionLink(models.Model):
    statement = models.ForeignKey('Statement')
    concession = models.ForeignKey('Concession')

    class Meta:
        managed = False
        db_table = 'concession_link_table'

class ProjectLink(models.Model):
    statement = models.ForeignKey('Statement')
    project = models.ForeignKey('Project')

    class Meta:
        managed = False
        db_table = 'project_link_table'

class ContractLink(models.Model):
    statement = models.ForeignKey('Statement')
    contract = models.ForeignKey('Contract')

    class Meta:
        managed = False
        db_table = 'contract_link_table'
"""

class Search(models.Model):
    '''
    Represents one run of any of the data-searching code
    '''
    label = models.CharField(max_length=10, primary_key=True)
    metadata = models.JSONField(type=dict)

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
        managed = False
        db_table = 'commodity_table'

    def __str__(self):
        return self.commodity_name or '<untitled>'


class CompanyAlias(models.Model):
    company_alias = models.CharField(primary_key=True, max_length=200, default=random_id)
    company_id = models.CharField(max_length=200)

    class Meta:
        managed = False
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

    class Meta:
        #managed = False
        db_table = 'company_table'

    def __str__(self):
        return self.company_name or '<untitled>'


class ConcessionAlias(models.Model):
    concession_alias = models.CharField(primary_key=True, max_length=200)
    concession_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'concession_alias_table'

    def __str__(self):
        return self.concession_alias or '<untitled>'


class Concession(models.Model):
    concession_id = models.CharField(primary_key=True, max_length=200)
    concession_name = models.CharField(max_length=200)
    unep_geo_id = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'concession_table'

    def __str__(self):
        return self.concession_name or '<untitled>'



class Contract(models.Model):
    contract_id = models.CharField(primary_key=True, max_length=200)
    doc = models.ForeignKey('Document')
    country = models.CharField(max_length=200)
    sign_date = models.CharField(max_length=200)
    title_type = models.CharField(max_length=200, blank=True)
    source_url = models.CharField(max_length=200)
    doc_cloud_id = models.CharField(max_length=200)
    doc_cloud_url = models.CharField(max_length=200)
    sign_year = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'contract_table'

    def __str__(self):
        return self.contract_id or '<untitled>'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Document(models.Model):
    doc_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    host_url = models.CharField(max_length=200, default='')
    source_url = models.CharField(max_length=200, default='')

    class Meta:
        managed = False
        db_table = 'document_table'

    def __str__(self):
        return self.host_url or '<untitled>'



class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    project_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'project_table'


    def __str__(self):
        return self.project_name or '<untitled>'


class Statement(models.Model):
    statement_id = models.CharField(primary_key=True, max_length=200, default=random_id)
    doc = models.ForeignKey(Document)
    statement_content = models.CharField(max_length=200)
    definitive = models.BooleanField(default=False)

    projects = models.ManyToManyField('Project', db_table='project_link_table', blank=True)
    companies = models.ManyToManyField('Company', db_table='company_link_table', blank=True)
    concessions = models.ManyToManyField('Concession', db_table='concession_link_table',
                                         blank=True)
    contracts = models.ManyToManyField('Contract', db_table='contract_link_table',
                                      blank=True)

    class Meta:
        managed = False
        db_table = 'statement_table'

    def __str__(self):
        return self.statement_content or '<untitled>'

"""

class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name or '<untitled>'

class License(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name or '<untitled>'


class Statement(models.Model):
    name = models.CharField(max_length=200)
    document = models.ForeignKey('Document')
    
    snippet = models.TextField()

    # when somebody reviews a statement, they set confidence
    # the system also adds the date they modified it
    confidence = models.FloatField() # should be between 0 and 100
    reviewed = models.DateField(blank=True, null=True) 
    # reviewed should be auto-update-date, but one that automated scripts can skip
    
    licenses = models.ManyToManyField('License')
    projects = models.ManyToManyField('Project')
    companies = models.ManyToManyField('Company')

    def __str__(self):
        return self.name or '<untitled>'


class Project(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50, blank=True) # should be choice
    # location -- should be some kind of geoid?

    def __str__(self):
        return self.name or '<untitled>'

class Document(models.Model):
    title = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    source_url = models.URLField() # official source, eg. on EDGAR
    mirror_url = models.URLField() # our copy of it, eg on S3
    

    def __str__(self):
        return self.title or '<untitled>'


"""
