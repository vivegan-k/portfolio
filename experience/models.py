from django.db import models

class Experience(models.Model):
    project_name = models.CharField(max_length= 200)
    company_name = models.CharField(max_length=200)
    languages = models.CharField(max_length= 200)
    description = models.CharField(max_length= 1000)
    contribution = models.CharField(max_length=1000)
    client = models.CharField(max_length=200)
