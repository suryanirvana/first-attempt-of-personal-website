from django.db import models

# Create your models here.


class ClassYear(models.Model):
    CLASSYEAR = [
        ('2019','2019'),
        ('2018', '2018'),
        ('2017','2017'),
        ('2016','2016'),
        ('2015','2015'),
        ('Other','Other'),
    ]
    classYear = models.CharField(max_length=6, choices=CLASSYEAR, default='2018')

    def __str__(self):
        return self.classYear

class Friend(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    ClassYear = models.ForeignKey(ClassYear, on_delete=models.CASCADE, default='Fasilkom')
    hobby = models.CharField(max_length=255)
    food = models.CharField(max_length=255)
    drink = models.CharField(max_length=255)

    def __str__(self):
        return self.name
