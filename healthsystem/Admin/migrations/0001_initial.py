# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('guardian', models.CharField(max_length=512)),
                ('doctor_refer', models.CharField(blank=True, max_length=512, null=True)),
                ('email', models.CharField(blank=True, max_length=512, null=True)),
                ('mobile', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('designation', models.CharField(max_length=512)),
                ('consultant', models.CharField(choices=[(b'Aesthetic and Reconstructive Surgery', b'Aesthetic and Reconstructive Surgery'), (b'Cardiology', b'Cardiology'), (b'Nephrology', b'Nephrology'), (b'Urology', b'Urology'), (b'ENT', b'ENT'), (b'Internal Medicine', b'Internal Medicine'), (b'Cardiac Surgery', b'Cardiac Surgery'), (b'Bariatric Surgery', b'Bariatric Surgery'), (b'Orthopaedics', b'Orthopaedics'), (b'Neurology', b'Neurology'), (b'Neurosurgery', b'Neurosurgery'), (b'Surgical Gastroenterology', b'Surgical Gastroenterology'), (b'Liver Transplantation', b'Liver Transplantation'), (b'Infectious Disease', b'Infectious Disease'), (b'Pain Management', b'Pain Management'), (b'Breast Surgery', b'Breast Surgery'), (b'Dental Surgery', b'Dental Surgery'), (b'Dermatology', b'Dermatology'), (b'Diabetology', b'Diabetology'), (b'Dietary', b'Dietary'), (b'Endocrinology', b'Endocrinology'), (b'Gastroenterology', b'Gastroenterology'), (b'General Surgery', b'General Surgery'), (b'Geriatric Medicine', b'Geriatric Medicine'), (b'Haematology', b'Haematology'), (b'Hepatology', b'Hepatology'), (b'Interventional Radiology', b'Interventional Radiology'), (b'Podiatry', b'Podiatry'), (b'Psychiatry', b'Psychiatry'), (b'Pulmonology', b'Pulmonology'), (b'Rheumatology', b'Rheumatology'), (b'Vascular Surgery', b'Vascular Surgery'), (b'Medical Oncology', b'Medical Oncology'), (b'Pediatric Immunology', b'Pediatric Immunology'), (b'Ophthalmology', b'Ophthalmology'), (b'Pediatric Endocrinology', b'Pediatric Endocrinology'), (b'Psychology', b'Psychology'), (b'Obstetrics and Gynaecology', b'Obstetrics and Gynaecology'), (b'Cardiology Electrophysiology ', b'Cardiology Electrophysiology '), (b'Surgical Oncology ', b'Surgical Oncology '), (b'Robotic Surgery', b'Robotic Surgery')], max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.CharField(blank=True, max_length=512, null=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(choices=[(b'Tablet', b'Tablet'), (b'Syrup', b'Syrup'), (b'Injection', b'Injection'), (b'Shampoo', b'Shampoo'), (b'Capsule', b'Capsule'), (b'Not Define', b'Not Define')], default=b'Not Define', max_length=25)),
                ('generic', models.CharField(blank=True, max_length=512, null=True)),
                ('batch_no', models.CharField(blank=True, max_length=512, null=True)),
                ('company', models.CharField(max_length=512)),
                ('supply_date', models.DateField()),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('mobile', models.BigIntegerField()),
                ('email', models.CharField(blank=True, max_length=512, null=True)),
                ('company', models.CharField(max_length=512)),
                ('company_address', models.TextField(blank=True, null=True)),
                ('supply_date', models.DateField()),
                ('supplier_address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('medicine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='Admin.Medicine')),
            ],
        ),
    ]
