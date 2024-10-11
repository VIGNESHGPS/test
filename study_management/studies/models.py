from django.db import models
from django.utils import timezone

class Study(models.Model):
    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    study_name = models.CharField(max_length=255)
    sponsor_name = models.CharField(max_length=255)
    study_description = models.TextField()
    study_phase = models.CharField(max_length=50, choices=PHASE_CHOICES)

    def __str__(self):
        return self.study_name
# Create your models here.
