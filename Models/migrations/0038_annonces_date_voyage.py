# Generated by Django 4.2.6 on 2024-08-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0037_remove_annonces_evaluation_annonces_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonces',
            name='date_voyage',
            field=models.DateField(default=None),
        ),
    ]
