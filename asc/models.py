from crum import get_current_user
from django.db import models
from personnel.models import Personnel
from district.models import Site
from django.urls import reverse


class Asc(models.Model):
    SEXE_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )

    TYPE_CHOICES = (
        ('titulaire', 'Titulaire'),
        ('remplaçante', 'Remplaçante')
    )
    identifiant = models.CharField(max_length=255, unique=True)
    ancien_id = models.CharField(max_length=60, unique=True, null=True, blank=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=155)
    sexe = models.CharField(max_length=2, choices=SEXE_CHOICES)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    contact = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='image/ASCs/', null=True, blank=True)
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
        super(Asc, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('asc:asc_detail', args=[
            self.identifiant
        ])

    class Meta:
        verbose_name_plural = 'Asc'

    def __str__(self):
        return f"{self.nom} {self.prenom}"

