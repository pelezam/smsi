import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class Fonction(models.Model):
    libelle = models.CharField(max_length=255)

    def __str__(self):
        return self.libelle


class Personnel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    SEX_CHOICES = (
        ('m', 'M'),
        ('f', 'F')
    )
    sexe = models.CharField(choices=SEX_CHOICES, max_length=5)
    contact = models.CharField(max_length=60)
    fonction = models.ForeignKey(Fonction, on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='media/photos_agents/', null=True, blank=True)

    def __str__(self):
        return self.username
