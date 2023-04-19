from django.urls import path
from . import views


urlpatterns =[
    path("" , views.home , name='home'),
    path("test/" , views.test , name='test'),
    # path("result/" , views.test , name='result'),
    path("Upload File/" , views.UploadFile , name='Upload File'),
    # path("shareresult/" , views.shareresult, name='shareresult'),
    path("contactus/" , views.contactus , name='contactus'),
    path("login/" , views.login , name= 'login'),
    path("signup/" , views.signup , name= 'signup'),
    path('result/<str:sentiment>/', views.result, name='result'),
    # path('analyze_file/', views.analyze_file, name='analyze_file'),
    path('analyze_file/dashboard/', views.analyze_file, name='dashboard'),
    path('logout/',views.logout,name='logout'),
]