from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    

class project(models.Model):
    project_title = models.CharField(max_length=20)
    project_text = models.TextField()
    