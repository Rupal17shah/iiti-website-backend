from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.title
        