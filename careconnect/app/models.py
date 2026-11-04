from django.db import models



class Doctor(models.Model):
    name=models.CharField(max_length=20)
    SPECIALIZATION_OPTIONS = (
    ("cardiology", "Cardiology"),
    ("dermatology", "Dermatology"),
    ("endocrinology", "Endocrinology"),
    ("ent", "Ear, Nose & Throat (ENT)"),
    ("gastroenterology", "Gastroenterology"),
    ("general_medicine", "General Medicine / Internal Medicine"),
    ("general_surgery", "General Surgery"),
    ("gynecology", "Gynecology & Obstetrics"),
    ("hematology", "Hematology"),
    ("nephrology", "Nephrology"),
    ("neurology", "Neurology"),
    ("oncology", "Oncology"),
    ("ophthalmology", "Ophthalmology"),
    ("orthopedics", "Orthopedics"),
    ("pediatrics", "Pediatrics"),
    ("psychiatry", "Psychiatry"),
    ("pulmonology", "Pulmonology"),
    ("radiology", "Radiology"),
    ("urology", "Urology"),
    ("other", "Other"),
    )
    specialization=models.CharField(max_length=20,choices=SPECIALIZATION_OPTIONS)
    fee=models.IntegerField()
    qualification=models.CharField(max_length=50)
    email=models.CharField(max_length=50)