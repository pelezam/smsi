from django.contrib import messages

DISTRICT_CHOICES = (
    ('kozah', 'Kozah'),
    ('bassar', 'Bassar'),
    ('binah', 'Binah'),
    ('danpken', 'Dankpen'),
    ('doufelgou', 'Doufelgou'),
    ('kéran', 'Kéran'),
)


def display_errors(request, form):
    if form.errors:
        print(form.errors)
        for field in form:
            if field.errors:
                for error in field.errors:
                    messages.error(request, str(error))
