from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.
class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NB = 'NB'
    PRIVATE = 'X'
    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (NB, 'non-binary/other'),
        (PRIVATE, 'prefer not to answer'),
    )
    SCHOOL_CHOICES = (
        ('AAHS', 'Allied Health'),
        ('AIT', 'Academy for Information Technology'),
        ('APA', 'Academy for Performing Arts'),
        ('MHS', 'Magnet High School'),
        ('UCT', 'UCTech'),
    )
    YEAR_CHOICES = [ (str(y),str(y)) for y in range(datetime.datetime.now().year, datetime.datetime.now().year + 6)]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=4, choices=SCHOOL_CHOICES, blank=True, null=True)
    grad_year = models.CharField(max_length=4, choices=YEAR_CHOICES, blank=True, null=True)
    # is_active = models.BooleanField(default=True)
       

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()