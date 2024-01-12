from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Teacher
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Teacher.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
