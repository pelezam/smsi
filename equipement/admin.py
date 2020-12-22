from django.contrib import admin
from .models import *


@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'quantity', 'echeance', 'periode', 'created_by', 'updated_by', 'created_at', 'updated_at')


@admin.register(Approvisionnement)
class ApprovisionementAdmin(admin.ModelAdmin):
    list_display = ('equipement', 'quantity_add', 'quantity_stock_debut', 'quantity_stock_fin', 'created_by',
                    'updated_by', 'created_at', 'updated_at')
    search_fields = ('equipement__libelle', )
