from django.db import models

class Archive(models.Model):
    class TypeChoices(models.TextChoices):
        VIDEO = "Video"
        ARCHIVE = "Archive"
        GENERIC = "Generic"
    user = models.CharField() # Será substituído pelo usuário abstrato do Django
    name = models.CharField(max_length=42)
    url = models.URLField()
    archive = models.FileField(upload_to='downloads/', null=True, blank=True)
    type = models.CharField(choices=TypeChoices.choices, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name