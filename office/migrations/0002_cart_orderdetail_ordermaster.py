# Generated by Django 5.1.1 on 2025-01-03 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
        ('owner', '0029_remove_company_bill_company_and_more'),
        ('sunil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('total_amount', models.FloatField(default=0)),
                ('qty', models.IntegerField()),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='office.item')),
                ('shpoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0, null=True)),
                ('total_price', models.FloatField(default=0, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('order_filter', models.IntegerField(default=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='office.item')),
                ('shpoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('order_filter', models.IntegerField(default=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
                ('shpoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
    ]
