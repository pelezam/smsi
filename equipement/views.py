from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Equipement, Approvisionnement
from .forms import EquipmentForm, ApproForm
from django.contrib import messages
from district.utils import display_errors
from django.http import JsonResponse


@login_required
def equipement_list(request):
    eqps = Equipement.objects.all()
    form = EquipmentForm()
    appro_form = ApproForm()
    return render(request, 'equipement/equipement-list.html', {"eqps": eqps, "form": form, "appro_form": appro_form})


@login_required
def equipement_edit(request, id):
    equipement = Equipement.objects.get(id=id)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            display_errors(request, form)
    return redirect('equipement:list')


@login_required
def equipement_detail(request, id):
    equipement = Equipement.objects.get(id=id)
    if request.is_ajax():
        data = {
            "id": equipement.id,
            "libelle": equipement.libelle.capitalize(),
            "description": equipement.description,
            "quantity": equipement.quantity,
            "echeance": equipement.echeance,
            "periode": equipement.periode,
        }
        return JsonResponse(data)
    return redirect('equipement:list')


@login_required
def equipement_create(request):
    eqps = Equipement.objects.all()
    form = EquipmentForm()
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            display_errors(request, form)
    return redirect('equipement:list')


@login_required
def approvisionement_create(request):
    if request.method == "POST":
        form = ApproForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('equipement:list')


@login_required
def approvisionement_list(request, id):
    equipement = Equipement.objects.get(id=id)
    approvis = Approvisionnement.objects.filter(equipement_id=id).order_by('-created_at')
    return render(request, 'equipement/equipement-approvisionnement.html', locals())