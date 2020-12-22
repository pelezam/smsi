from django.contrib.auth.decorators import login_required
from .models import Attribution
from django.http import JsonResponse
from django.shortcuts import render


@login_required
def attribution_detail(request, id):
    attr = Attribution.objects.get(id=id)

    if request.is_ajax():
        data = {
            "id": attr.id,
            "asc": attr.asc.id,
            "equipement": attr.equipement.id,
            "date_attribution": attr.date_attribution,
            "quantity": attr.quantity,
            "date_renouvellement": attr.date_renouvellement,
            "status_renouvellement": attr.status_renouvellement,
        }
    return JsonResponse(data)
