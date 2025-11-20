from django.db import models

class StudentApplication(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100)
    country_of_residence = models.CharField(max_length=100, blank=True, null=True)
    
    highest_academic_qualification = models.CharField(max_length=255, blank=True, null=True)
    name_of_institution = models.CharField(max_length=255, blank=True, null=True)
    year_of_completion = models.PositiveIntegerField(blank=True, null=True)

    current_occupation = models.CharField(max_length=255, blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)

    how_you_heard_about_us = models.CharField(max_length=255, blank=True, null=True)
    anything_else = models.TextField(blank=True, null=True)

    academic_certificate = models.FileField(upload_to='applications/certificates/')
    passport_photo = models.ImageField(upload_to='applications/photos/')
    national_id = models.FileField(upload_to='applications/ids/', null=True, blank=True)
    passport = models.FileField(upload_to='applications/passports/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"{self.full_name} ({self.email})"
