# Generated by Django 3.0.11 on 2020-11-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributionsite',
            name='nb_asc',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
