from django.db import models
from django.contrib.auth.models import User

class Archive(models.Model):
    class TypeChoices(models.TextChoices):
        VIDEO = "Video"
        ARCHIVE = "Archive"
        GENERIC = "Generic"
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=42)
    url = models.URLField()
    archive = models.FileField(upload_to='downloads/', null=True, blank=True)
    type = models.CharField(choices=TypeChoices.choices, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name