# Generated by Django 3.0.11 on 2020-11-16 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
        ('asc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributionSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('nb_asc', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('equipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipement.Equipement')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.Site')),
            ],
        ),
        migrations.CreateModel(
            name='Attribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_attribution', models.DateField(default=django.utils.timezone.now)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('date_renouvellement', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('asc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asc.Asc')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='attribution_created', to=settings.AUTH_USER_MODEL)),
                ('equipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipement.Equipement')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attribution_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
