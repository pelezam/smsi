# Generated by Django 3.0.11 on 2020-11-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribution', '0002_auto_20201116_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribution',
            name='status_renouvellement',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='attributionsite',
            name='nb_asc',
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
    ]
