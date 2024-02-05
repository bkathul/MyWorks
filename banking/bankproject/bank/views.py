from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Index
def index(request):
    return render(request,'index.html')

# DetailForm
