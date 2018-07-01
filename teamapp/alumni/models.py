from django.db import models
import datetime

# Create your models here.
class Alum(models.Model):
    AAHS = 'aahs'
    AIT = 'ait'
    APA = 'apa'
    MHS = 'mhs'
    UCT = 'uct'
    YEAR_CHOICES = [ (y,y) for y in range(2003, datetime.datetime.now().year + 1)]

    SCHOOL_CHOICES = (
        (AAHS, 'Allied Health'),
        (AIT, 'Academy for Information Technology'),
        (APA, 'Academy for Performing Arts'),
        (MHS, 'Magnet High School'),
        (UCT, 'UCTech'),
    )

    first = models.CharField(max_length=40)
    last = models.CharField(max_length=40)
    current_name = models.CharField(max_length=50, blank=True, null=True)
    grad_year = models.CharField(max_length=4, choices=YEAR_CHOICES, blank=True, null=True)
    school = models.CharField(max_length=4, choices=SCHOOL_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)