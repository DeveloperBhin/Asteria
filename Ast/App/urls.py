
from django.urls import path
from . import views


urlpatterns = [
   path('',views.index,name='index'),
   path('DocReport/',views.DocReport,name='DocReport'),
   path('Attendance/',views.Attendance,name='Attendance'),
   path('Update/',views.Update,name='Update'),
   path('register/',views.PatientRegView,name='register'),
   path('Notification/',views.Notification,name='Notification'),
   path('Login/',views.Login,name='Login'),
   path('Dashboard/',views.Dashboard,name='Dashboard'),
  path('AdminDashboard/',views.AdminDashboard,name='AdminDashboard'),
  path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
  path('Adminregister/',views.AdminRegView,name='Adminregister'),
  
  
  
  
  
   
]

