from django.contrib import admin
from hulk.models import (
    Company, Concession, Document, Statement, Project,
    Commodity, ConcessionAlias, CompanyAlias)

for table in (Company, Concession, Document,Statement,Project,
              Commodity, ConcessionAlias, CompanyAlias):
    admin.site.register(table)

# Register your models here.
