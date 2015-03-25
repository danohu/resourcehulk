from django.contrib import admin
from hulk.models import (
    Company, Concession, Document, Statement, Project,
    Commodity, ConcessionAlias, CompanyAlias,
    Search,SearchResult)

for table in (Company, Concession, Document,Statement,Project,
              Commodity, ConcessionAlias, CompanyAlias,
              Search, SearchResult):
    admin.site.register(table)

# Register your models here.
