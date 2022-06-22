from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    # path('', views.index, name='index'),
    path('doctorclick', views.doctorclick),
    
    path('doctorsignup', views.doctor_signup,name='doctor/signup'),
    
    path('doctorlogin', LoginView.as_view(template_name='doctor/login.html')),
    
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    
    path('doctor-dashboard', views.doctor_dashboard,name='doctor-dashboard'),
    path('search', views.search,name='search'),
    
    path('doctor-patient', views.doctor_patient,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient,name='doctor-view-patient'),

    
    
    
]