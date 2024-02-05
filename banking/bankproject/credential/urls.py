from .import views
from django.urls import path
app_name='credential'

urlpatterns =[
    path('register',views.register,name='register'),
    path('login',views.loginn,name='login'),
    path('logout',views.logout,name='logout'),
    path('welcome',views.welcome,name='welcome'),
    path('success',views.success,name='success'),
    path('details',views.detail_form,name='detail_form'),
]