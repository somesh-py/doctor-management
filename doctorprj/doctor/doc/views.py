from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Doctor
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'index.html')


def registration(request):
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
            return redirect('/')
        elif Doctor.objects.filter(contact=contact).exists():
            messages.error(request, 'contatc number already exist')
            return redirect('/')
        else:
            Doctor.objects.create(name=name, degree=degree, contact=contact,
                                  email=email, password=password, image=imaged, catagory=catagory)
            messages.success(request, 'registration done sucessfully')
            return redirect('/login/')


def login(request):
    return render(request, 'login.html')


def logindata(request):
    if request.method == 'POST':
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        if Doctor.objects.filter(email=email).exists():
            if Doctor.objects.filter(contact=contact).exists():
                i_email = Doctor.objects.get(email=email)
                i_password = i_email.password
                if check_password(password, i_password):
                    messages.success(request, 'loginsucessfully')
                    return redirect('/table/')
                else:
                    messages.error(request, 'password was incorrect')
                    return redirect('/login/')
            else:
                messages.error(request, 'contact error')
                return redirect('/login/')
        else:
            messages.error(request, 'email not exist put correct email')
            return redirect('/login/')


def table(request):
    doctordata = Doctor.objects.all()
    return render(request, 'table.html', {'ddata': doctordata})


def update(request, tid):
    tid = Doctor.objects.get(id=tid)
    return render(request, 'update.html', {'id': tid})


def updatedata(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        contact = request.POST.get('contact')
        password = make_password(request.POST.get('password'))
        email = request.POST.get('email')
        catagory = request.POST.get('catagory')
        image=request.FILES.get('image')
        if Doctor.objects.filter(id=tid).exists():
            Doctor.objects.update(name=name,degree=degree,contact=contact,password=password,email=email,catagory=catagory,image=image)
            return redirect('/table/')
            
def delete(request,tid):
    Doctor.objects.filter(id=tid).delete()
    return redirect('/table/')