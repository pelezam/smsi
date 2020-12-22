from crum import get_current_user
from django.db import models
from .utils import DISTRICT_CHOICES
from personnel.models import Personnel


class Site(models.Model):
    libelle = models.CharField(max_length=255, unique=True)
    district = models.CharField(max_length=255, choices=DISTRICT_CHOICES)
    created_by = models.ForeignKey(Personnel, on_delete=models.PROTECT, editable=False,
                                   related_name='%(class)s_created')
    updated_by = models.ForeignKey(Personnel, on_delete=models.PROTECT, editable=False,
                                   related_name='%(class)s_updated',
                                   null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(Site, self).save(*args, **kwargs)

    def __str__(self):
        return self.libelle

