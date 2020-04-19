from django.db import models

# Create a blog models

# Add the blog app to the settings

# Create a migration

# Migrate

# Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length= 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# class Experience(models.Model):
#     project_name = models.CharField(max_length= 200)
#     company_name = models.CharField(max_length=200)
#     languages = models.CharField(max_length= 200)
#     description = models.CharField(max_length= 1000)
#     contribution = models.CharField(max_length=1000)

