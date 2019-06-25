from django.db import models
from django.urls import reverse

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True)# Defines the pages title and max length
    content = models.TextField()
    counter = models.IntegerField(default = 1) # defines the word counter using and interger which is default to 1.

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('wiki:detail', args=[self.title])


class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='uploads/') #Creates file filed for the forms.py and file upload page

    def __str__(self):
        return self.upload.name

