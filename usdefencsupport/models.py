from django.db import models

# Create your models here.

class TrackSoldier(models.Model):
    profile = models.ImageField(upload_to='usdefencsupport/img/')
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    Rank = models.CharField(max_length=200)
    Height = models.DecimalField(decimal_places=2, max_digits=200)
    kids = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=200)
    grade_a = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    grade_b = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class RequestCall(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_carrier = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    minute_requested = models.CharField(max_length=200)
    country_of_deploy = models.CharField(max_length=200)
    name_of_soldier = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class FlightBooking(models.Model):
    passenger_name = models.CharField(max_length=200)
    soldier_name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departure_date = models.DateField()
    contact_email = models.EmailField()
    passport_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.passenger_name} → {self.destination}"

class MedicalReport(models.Model):
    soldier_name = models.CharField(max_length=200)
    reporter_name = models.CharField(max_length=200)
    email = models.EmailField()
    injury_description = models.TextField()
    treatment_given = models.TextField()
    estimated_bill = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Medical Report for {self.soldier_name}"
