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
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    birthdate = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=True)
    is_alum = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)   

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()