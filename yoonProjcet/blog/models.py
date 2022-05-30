from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
       return self.title
    
    def summary(self): #글자수 제한
        return self.body[:100]
