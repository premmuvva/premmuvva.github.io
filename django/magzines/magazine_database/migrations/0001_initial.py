# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-31 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Invoices',
            fields=[
                ('invoice_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_invoice', models.DateTimeField()),
                ('invoice_amount', models.IntegerField()),
                ('other_invoice_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Subscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_subscription_started', models.DateTimeField()),
                ('date_subscription_ended', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='', max_length=20)),
                ('customer_address', models.TextField(default='')),
                ('customer_phone', models.IntegerField()),
                ('customer_email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('other_customer_details', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_Line_Items',
            fields=[
                ('item_number', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('magazine_id', models.IntegerField()),
                ('date_magazine_delivered', models.DateTimeField()),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine_database.Customer_Invoices')),
            ],
        ),
        migrations.CreateModel(
            name='Magazine_Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplied_from_date', models.DateTimeField()),
                ('supplied_to_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Magazines',
            fields=[
                ('magazine_id', models.IntegerField(primary_key=True, serialize=False)),
                ('magazine_name', models.CharField(default='', max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ref_Frequencies',
            fields=[
                ('frequency_code', models.IntegerField(primary_key=True, serialize=False)),
                ('frequency_description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier_code', models.IntegerField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='magazines',
            name='publication_frequency_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine_database.Ref_Frequencies'),
        ),
        migrations.AddField(
            model_name='magazine_suppliers',
            name='magazine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine_database.Magazines'),
        ),
        migrations.AddField(
            model_name='magazine_suppliers',
            name='supplier_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine_database.Suppliers'),
        ),
        migrations.AddField(
            model_name='customer_subscriptions',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine_database.Customers'),
        ),
        migrations.AddField(
            model_name='customer_subscriptions',
            name='magazine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine_database.Magazines'),
        ),
        migrations.AddField(
            model_name='customer_invoices',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine_database.Customers'),
        ),
        migrations.AlterUniqueTogether(
            name='magazine_suppliers',
            unique_together=set([('magazine_id', 'supplier_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='invoice_line_items',
            unique_together=set([('invoice_id', 'item_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='customer_subscriptions',
            unique_together=set([('customer_id', 'magazine_id')]),
        ),
    ]