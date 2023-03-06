from django.db import models
from people.models import People

# Create your models here.
class Research(models.Model):
    specialization = models.CharField(max_length=50)
    person = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.person


class Labs(models.Model):
    name = models.CharField(max_length=5000)
    person = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.name


class Papers(models.Model):
    person = models.CharField(max_length=500)
    year = models.IntegerField()
    paper = models.CharField(max_length=100)

    def __str__(self):
        return self.person


class Projects(models.Model):
    title = models.CharField(max_length=500)
    worker = models.CharField(max_length=500)
    funding = models.CharField(max_length=500)
    duration = models.CharField(max_length=50)
    project_type = models.CharField(max_length=500)

    def __str__(self):
        return self.title
