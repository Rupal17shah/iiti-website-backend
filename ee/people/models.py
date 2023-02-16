from django.db import models
# Create your models here.


class People(models.Model):
    people_type = [('Staff', 'staff'),
                   ('Faculty', 'faculty'),
                   ('Phd', 'Phd'),
                   ('MTech', 'MTech'),
                   ('BTech', 'BTech'),
                   ('Alumni', 'Alumni')
                   ]
    people_cat = models.CharField(choices=people_type, max_length=20)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    details = models.CharField(max_length=10000)
    link = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name
