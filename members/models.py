from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    Age = models.IntegerField(max_length=30)
    email = models.EmailField(max_length=255)
    joined_date = models.DateField();

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

