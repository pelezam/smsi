from crum import get_current_user
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.core.exceptions import ValidationError
from asc.models import Asc
from equipement.models import Equipement
from django.utils import timezone
from personnel.models import Personnel
from .utils import calculate_renouvellement
from asc.models import Site


class AttributionSite(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    nb_asc = models.PositiveIntegerField(null=True, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        nb_asc = Asc.objects.filter(site_id=self.site.id).count()
        self.nb_asc = nb_asc
        super(AttributionSite, self).save(*args, **kwargs)

    def __str__(self):
        return f"attribution au site de {self.site.libelle}"


class Attribution(models.Model):
    asc = models.ForeignKey(Asc, on_delete=models.CASCADE)
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    date_attribution = models.DateField(default=timezone.now)
    quantity = models.PositiveIntegerField(default=1)
    date_renouvellement = models.DateField(null=True, blank=True)
    status_renouvellement = models.BooleanField(default=False, null=True, blank=True)
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
        self.date_renouvellement = calculate_renouvellement(self.date_attribution, self.equipement)
        super(Attribution, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.asc.nom} {self.asc.prenom}"


class Remplacement(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    motif = models.TextField()
    attribution = models.ForeignKey(Attribution, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.attribution.equipement.libelle}, date de replacement: {self.created_at}"


def attribution_save(sender, instance, **kwargs):
    equipement = Equipement.objects.get(id=instance.equipement_id)
    equipement.quantity -= instance.quantity
    equipement.save()


def attribution_delete(sender, instance, **kwargs):
    equipement = Equipement.objects.get(id=instance.equipement_id)
    equipement.quantity += instance.quantity
    equipement.save()


post_save.connect(attribution_save, sender=Attribution)
post_delete.connect(attribution_delete, sender=Attribution)
# pre_save.connect(attribution_pre_save, sender=Attribution)