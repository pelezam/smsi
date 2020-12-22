from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from asc.models import Asc
from attribution.forms import AttibutionForm
from district.utils import display_errors
from .forms import AscForm
from attribution.models import Attribution
from django.contrib import messages
from django.http import JsonResponse


@login_required
def asc_list(request):
    ascs = Asc.objects.all()
    form = AscForm()
    return render(request, 'asc/list_asc.html', {"ascs": ascs, "form": form})


@login_required
def asc_create(request):
    form = AscForm()
    if request.method == "POST":
        form = AscForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Opération effectuée avec succès')
        else:
            display_errors(request, form)
    return redirect('asc:asc_list')


@login_required
def asc_edit(request, id):
    asc = Asc.objects.get(identifiant=id)
    if request.method == "POST":
        form = AscForm(request.POST, request.FILES, instance=asc)
        if form.is_valid():
            form.save()
            messages.success(request, 'Opération effectuée avec succès')
        else:
            display_errors(request, form)
    return redirect('asc:asc_list')


@login_required
def asc_detail(request, id):
    asc = Asc.objects.get(identifiant=id)
    if request.is_ajax():
        data = {
            "id": asc.id,
            "identifiant": asc.identifiant,
            "ancien_id": asc.ancien_id,
            "nom": asc.nom,
            "prenom": asc.prenom,
            "sexe": asc.sexe,
            "site": str(asc.site.id),
            "type": asc.type,
            "contact": asc.contact,
            "photo": asc.photo.url if asc.photo else ""
        }
        return JsonResponse(data)
    attr_form = AttibutionForm()
    attrs = Attribution.objects.filter(asc_id=asc.id)
    return render(request, 'asc/detail_asc.html', {'asc': asc, 'attr_form': attr_form, 'attrs': attrs})


@login_required
def asc_attribution(request, id):
    form = AttibutionForm()
    asc = Asc.objects.get(identifiant=id)
    if request.method == "POST":
        form = AttibutionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Opération effectuée avec succès')
        else:
            display_errors(request, form)
    return redirect('asc:asc_detail', id=asc.identifiant)


@login_required
def asc_attribution_delete(request, id, id_attr):
    asc = Asc.objects.get(identifiant=id)
    attr = Attribution.objects.get(id=id_attr)
    attr.delete()
    messages.success(request, 'Opération effectuée avec succès')
    return redirect('asc:asc_detail', id=asc.identifiant)
