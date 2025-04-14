from django.shortcuts import render,redirect
from .models import *
from .forms import * 
from django.contrib.auth import logout,login,authenticate



def index(request):
    return render(request, 'index.html')

def PatientRegView(request):
    if request.method == 'POST':
        pateintreg = PatientRegForm(request.POST)
        if pateintreg .is_valid():
            pateintreg.save()
            
            return redirect('Login')
        else:
         print(pateintreg .errors)
     
      
    else: 
     pateintreg  = PatientRegForm()
    
        
    
    context={
        'pateintreg':pateintreg 
       
    }
    
    return render(request, 'register.html',context)


def Login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = PatientReg.objects.get(username=username)
                if user.check_password(password):  # Uses hashed password comparison
                    request.session['patient_id'] = user.id
                    return redirect('Dashboard')
                else:
                    form.add_error(None, 'Invalid username or password')
            except PatientReg.DoesNotExist:
                form.add_error(None, 'Invalid username or password')
    else:
        form = PatientLoginForm()

    return render(request, 'Login.html', {'form': form})

def AdminRegView(request):
    if request.method == 'POST':
        Adminpg = AdminRegForm(request.POST)
        if Adminpg.is_valid():
            Adminpg.save()
            return redirect('AdminLogin')
        
    else:
        Adminpg = AdminRegForm()    
        
        
     
    
    return render(request,'AdminReg.html',{'Adminpg':Adminpg})

def AdminLogin(request):
    if request.method == 'POST':
       Loginform = AdminLoginForm(request.POST)
       if Loginform.is_valid():
        
        username = Loginform.cleaned_data['username']
        password = Loginform.cleaned_data['password']
       
       try:
           user = AdminPage.objects.get(username=username)
           
           if user.check_password(password):
              request.session['Admin_id'] = user.id
              if user.Role=='Admin':
              
               return redirect('AdminDashboard') 
              else:
               return redirect('index')
           else:
               Loginform.add_error(None,'Invalid Username or Password')
               
       except AdminPage.DoesNotxist:
             Loginform.add_error(None,'Invalid Username or Password')
             
            
    else:
        Loginform = AdminLoginForm()
        
    context = {
        'Loginform':Loginform
    }             
        
    return render(request,'AdminLogin.html',context)


def DocReport(request):
    
    return render(request, 'DocReport.html')
def Attendance(request):
    return render(request, 'Attendance.html')
def Notification(request):
    return render(request,'Notification.html')
def Update(request):
    return render(request,'Update.html')
def Dashboard(request):
    return render(request,'ChildrenDashboard.html')

def AdminDashboard(request):
    return render(request,'AdminDashboard.html')

