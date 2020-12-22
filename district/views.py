from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Site
from .forms import SiteForm
from django.contrib import messages
from django.http import JsonResponse
from .utils import display_errors


@login_required
def site_list(request):
    form = SiteForm()
    sites = Site.objects.annotate(site_count=Count('asc'))
    return render(request, 'district/list_site.html', locals())


@login_required
def site_create(request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Opération effectuée avec succès')
        else:
            display_errors(request, form)
    return redirect('district:site_list')


@login_required
def site_edit(request, id):
    site = Site.objects.get(id=id)
    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuée avec succès')
        else:
            display_errors(request, form)
    return redirect('district:site_list')


@login_required
def site_detail(request, id):
    site = Site.objects.get(id=id)
    if request.is_ajax():
        data = {
            "id": site.id,
            "libelle": site.libelle.capitalize(),
            "district": site.district,
        }
        return JsonResponse(data)

    return redirect('district:site_list')
