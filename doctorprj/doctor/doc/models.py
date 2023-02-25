from django.db import models

# Create your models here.
CHOICE_COURSE=(
    ('bone','bone'),
    ('lungs','lungs'),
    ('kindey','kindey'),
    ('ear','ear'),
    ('eye','eye'),
)
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    image=models.ImageField(upload_to='docimage/')
    catagory=models.CharField(choices=CHOICE_COURSE,max_length=50)
    