from django.db import models
from django.contrib.auth.models import User

class Archive(models.Model):
    class TypeChoices(models.TextChoices):
        VIDEO = "Video"
        ARCHIVE = "Archive"
        #GENERIC = "Generic"
    class StatusChoice(models.TextChoices):
        FALHA = "Falha"
        PENDENTE = "Pendente"
        CONCLUIDO = "Concluído"
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=42)
    url = models.URLField(max_length=1000)
    archive = models.FileField(upload_to='downloads/', null=True, blank=True)
    type = models.CharField(choices=TypeChoices.choices, max_length=7, null=True, blank=True)
    status = models.CharField(choices=StatusChoice.choices, max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name