from django.contrib import admin
from .models import Attribution, AttributionSite
from .forms import AttributionSiteForm


@admin.register(Attribution)
class AttributionAdmin(admin.ModelAdmin):
    list_display = ('asc', 'equipement', 'date_attribution', 'quantity', 'date_renouvellement')


@admin.register(AttributionSite)
class AttributionSiteAdmin(admin.ModelAdmin):
    list_display = ('site', 'quantity', 'nb_asc')
    form = AttributionSiteForm
