from django.db import models
from django.db.models import permalink
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150, verbose_name='Gallery Image Title')
    added_date = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=True)
    project_image = models.ImageField(upload_to='projects')

    class Meta:
        ordering = ['-added_date']
        verbose_name_plural = "Projects"

    def __str__(self):
        return '%s' % self.name
