from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from .models import Doctor
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method=='POST':
        name=request.POST['name']
        degree=request.POST['degree']
        contact=request.POST['contact']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        image=request.POST['image']
        catagory=request.POST['catagory']
        if Doctor.objects.filter(email=email).exists():
            messages.error(request,'email already exist')
            return redirect('/')
        elif Doctor.objects.filter(contact=contact).exists():
            messages.error(request,'contatc number already exist')
            return redirect('/')
        else:
            Doctor.objects.create(name=name,degree=degree,contact=contact,email=email,password=password,image=image,catagory=catagory)
            messages.success(request,'registration done sucessfully')
            return redirect('/login/')
        
def login(request):
    return render(request,'login.html')
def logindata(request):
    if request.method=='POST':
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        if Doctor.objects.filter(email=email).exists():
            if Doctor.objects.filter(contact=contact).exists():
                i_email=Doctor.objects.get(email=email)
                i_password=i_email.password
                if check_password(password,i_password):
                    messages.success(request,'loginsucessfully')
                    return redirect('/login/')
                else:
                    messages.error(request,'password was incorrect')
                    return redirect('/login/')
            else:
                messages.error(request,'contact error')
                return redirect('/login/')
        else:
            messages.error(request,'email not exist put correct email')
            return redirect('/login/')