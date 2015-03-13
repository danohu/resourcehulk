from django.db import models


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


