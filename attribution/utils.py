from dateutil.relativedelta import *


def calculate_renouvellement(date_attribution, equipement):
    date_renouvellement  = None
    periode = equipement.periode
    echance = equipement.echeance

    if periode == "semaine":
        date_renouvellement = date_attribution + relativedelta(weeks=+echance)
    elif periode == "mois":
        date_renouvellement = date_attribution + relativedelta(months=+echance)
    elif periode == "annee":
        date_renouvellement = date_attribution + relativedelta(years=+echance)

    return date_renouvellement
