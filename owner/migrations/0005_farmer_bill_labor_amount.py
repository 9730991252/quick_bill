# Generated by Django 5.1.3 on 2024-11-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_farmer_bill_bill_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer_bill',
            name='labor_amount',
            field=models.FloatField(null=True),
        ),
    ]
