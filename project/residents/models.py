from django.db import models

class Residents(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.BigIntegerField()
    gender = models.CharField(max_length=255)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=255)
    civilstatus = models.CharField(max_length=255)
    bloodtype = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    totalhouseholdmember = models.BigIntegerField()
    occupation = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    educationalattainment = models.CharField(max_length=255)
    householdno = models.BigIntegerField()

    def __str__(self):
        return self.lastname
