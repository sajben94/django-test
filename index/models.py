from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=255,unique=True)
    url = models.URLField(unique=True)


    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
# Create your models here.

    def __str__(self):
        return self.first_name +" "+ self.last_name
