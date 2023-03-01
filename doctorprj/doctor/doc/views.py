from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    return render(request, 'login.html')


def logindata(request):
    if request.method == 'POST':
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        if Mainuser.objects.filter(email=email).exists():
            if Mainuser.objects.filter(contact=contact).exists():
                i_email = Doctor.objects.get(email=email)
                i_password = i_email.password
                if check_password(password, i_password):
                    doctordata = Doctor.objects.all()
                    return render(request, 'registration.html', {'ddata': doctordata})
                else:
                    messages.error(request, 'password was incorrect')
                    return redirect('/')
            else:
                messages.error(request, 'contact error')
                return redirect('/')
        else:
            messages.error(request, 'email not exist put correct email')
            return redirect('/')


@login_required(login_url='/')
def registration(request):
    return render(request, 'registration.html')


def registrationdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        imaged = request.FILES.get('imaged')
        catagory = request.POST.get('catagory')
        if Doctor.objects.filter(email=email).exists():
            messages.error(request, 'email already exist')
            return redirect('/reg/')
        elif Doctor.objects.filter(contact=contact).exists():
            messages.error(request, 'contatc number already exist')
            return redirect('/reg/')
        else:
            Doctor.objects.create(name=name, degree=degree, contact=contact,
                                  email=email, password=password, image=imaged, catagory=catagory)
            doctordata = Doctor.objects.all()
            return render(request, 'table.html', {'ddata': doctordata})


@login_required(login_url='/')
def table(request):
    doctordata = Doctor.objects.all()
    return render(request, 'table.html', {'ddata': doctordata})


def update(request, tid):
    tid = Doctor.objects.get(id=tid)
    dimg=Doctor.objects.all()
    return render(request, 'update.html', {'id': tid,'image':dimg})


def updatedata(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        contact = request.POST.get('contact')
        password = make_password(request.POST.get('password'))
        email = request.POST.get('email')
        catagory = request.POST.get('catagory')
        image = request.FILES.get('image')
        Doctor.objects.filter(id=tid).update(name=name, degree=degree, contact=contact,
                                             password=password, email=email, catagory=catagory, image=image)
        return redirect('/urltable/')


def delete(request, tid):
    Doctor.objects.filter(id=tid).delete()
    return redirect('/urltable/')


def urltable(request):
    doctordata = Doctor.objects.all()
    return render(request, 'table.html', {'ddata': doctordata})


def urlregistration(request):
    return render(request,'registration.html')
