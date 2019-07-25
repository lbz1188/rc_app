from django.db import models
from django.utils import timezone

# Create your models here.

class Resort(models.Model):
    resort = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)
    logo_dir = models.CharField(max_length=100)
    descption = models.TextField()
    date_update = models.DateField(default=timezone.now)

    def __str__(self):
        return str(f"|{self.resort}|{self.brief}|{self.date_update}|")