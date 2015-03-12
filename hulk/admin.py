from django.contrib import admin
from hulk.models import Company, License, Document, Statement, Project

for table in (Company, License, Document,Statement,Project):
    admin.site.register(table)

# Register your models here.
