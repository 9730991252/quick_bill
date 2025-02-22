# Generated by Django 5.1.3 on 2024-12-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("owner", "0016_company_bill"),
    ]

    operations = [
        migrations.AddField(
            model_name="company_bill",
            name="date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="company_bill",
            name="total_amount",
            field=models.FloatField(null=True),
        ),
    ]
