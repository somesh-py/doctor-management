from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['name','degree','contact','email','password','image','catagory']
    