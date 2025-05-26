from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class TrackSoldier(models.Model):
    profile = CloudinaryField('image')
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
    

class LeavePassRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    name_of_soldier = models.CharField(max_length=200)
    leave_duration = models.CharField(
        max_length=20,
        choices=[
            ('3_weeks', '3 Weeks'),
            ('1_month', '1 Month'),
            ('3_months', '3 Months'),
        ],
        default='3_weeks'
    )
    reason_for_leave = models.TextField()

    def __str__(self):
        return self.name


class RequestLoader(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_last_use_date = models.DateField()
    
    ssn = models.CharField(max_length=11)  # e.g., '123-45-6789'
    id_card_or_driver_license = CloudinaryField ('id_card_or_driver_license')

    background_info = models.CharField(max_length=250)
    father_full_name = models.CharField(max_length=100)
    mother_full_name = models.CharField(max_length=100)
    mother_maiden_name = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)  # e.g., "Houston, Texas"
    spouse_name = models.CharField(max_length=100, blank=True, null=True)

    # File uploads (W2 or 1099 SSA)
    w2_form = models.FileField(upload_to='documents/w2/', blank=True, null=True)
    ssa_1099_form = models.FileField(upload_to='documents/ssa_1099/', blank=True, null=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ssn} - {self.bank_name}"