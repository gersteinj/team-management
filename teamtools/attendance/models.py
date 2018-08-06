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
        if len(self.preferred) > 0:
            return self.preferred
        elif len(self.middle) > 0:
            return ' '.join((self.first, self.middle, self.last))
        else:
            return ' '.join((self.first, self.last))


class Entry(models.Model):
    """Attendance at a meeting"""

    date = models.DateField()

    enter_time = models.TimeField(auto_now_add=True)
    exit_time = models.TimeField(blank=True, null=True)

    person = models.ForeignKey(Person, on_delete=models.CASCADE)