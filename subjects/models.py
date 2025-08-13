from django.db import models
from django.conf import settings


class Subject(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  photo = models.ImageField(upload_to='subject_photos/', blank=True, null=True)
  
  teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subjects_taught', limit_choices_to={'teacher__isnull': False}, blank=True, null=True)
  
  def __str__(self):
    return self.name