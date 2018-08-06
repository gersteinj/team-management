from django.db import models

# Create your models here.
class Person(models.Model):
    uid = models.CharField(max_length = 30, primary_key=True)
    first = models.CharField(max_length=255)
    middle = models.CharField(max_length=255, blank=True)
    last = models.CharField(max_length=255)
    preferred = models.CharField(max_length=255, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uid