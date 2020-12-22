from django.db import models
from personnel.models import Personnel
from crum import get_current_user


class Equipement(models.Model):
    PERIODE_CHOICES = (
        ('semaine', 'SEMAINE'),
        ('mois', 'MOIS'),
        ('annee', 'ANNEE')
    )
    libelle = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(editable=False, default=0)
    echeance = models.PositiveIntegerField()
    periode = models.CharField(max_length=255, choices=PERIODE_CHOICES)
    created_by = models.ForeignKey(Personnel, on_delete=models.PROTECT, editable=False,
                                   related_name='%(class)s_created')
    updated_by = models.ForeignKey(Personnel, on_delete=models.PROTECT, editable=False,
                                   related_name='%(class)s_updated',
                                   null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.libelle

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(Equipement, self).save(*args, **kwargs)


class Approvisionnement(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    quantity_add = models.PositiveIntegerField()
    quantity_stock_debut = models.PositiveIntegerField(editable=False)
    quantity_stock_fin = models.PositiveIntegerField(editable=False)
    created_by = models.ForeignKey(Personnel, on_delete=models.PROTECT, editable=False,
                                   related_name='%(class)s_created')
    updated_by = models.ForeignKey(Personnel, on_delete=models.PROTECT, editable=False,
                                   related_name='%(class)s_updated',
                                   null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        try:
            equipement = Equipement.objects.get(id=self.equipement.id)
        except Equipement.DoesNotExist:
            pass
        else:
            if self.id:
                app = Approvisionnement.objects.get(id=self.id)
                equipement.quantity -= app.quantity_add
            self.quantity_stock_debut = equipement.quantity
            equipement.quantity += self.quantity_add
            equipement.save()
            self.quantity_stock_fin = equipement.quantity

        super(Approvisionnement, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.equipement.libelle} approvisioné de {self.quantity_add}"

