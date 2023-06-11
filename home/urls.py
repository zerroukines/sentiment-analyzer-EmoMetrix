from django.urls import path
from . import views


urlpatterns =[
    path("" , views.home , name='home'),
    path("test/" , views.test , name='test'),
    path("Upload File/" , views.UploadFile , name='Upload File'),
    path("analyze_comments/" , views.analyze_comments, name='analyze_comments'),
    path("contactus/" , views.contactus , name='contactus'),
    path("login/" , views.login , name= 'login'),
    path("signup/" , views.signup , name= 'signup'),
    path('result/<str:sentiment>/', views.result, name='result'),
    path('insert link/', views.insertlink, name='insert link'),
    path('analyze_file/dashboard/', views.analyze_file, name='dashboard'),
    path('logout/',views.logout,name='logout'),
]
handler404 = 'home.views.handler404'

