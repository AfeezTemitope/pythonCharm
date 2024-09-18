from django.db import models


class User (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')),)

    def __str__(self):
        return self.name

