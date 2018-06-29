from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES)
    birthdate = models.DateField()
    # is_active = models.BooleanField(default=True)
    # is_student = models.BooleanField()
    # is_alum = models.BooleanField()
    # is_mentor = models.BooleanField()   

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()