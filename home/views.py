from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text="Django Kurulumu: python -m pipi install -e django <br> Proje oluşturma: django-admin startproject mysite <br> App Ekleme: python manage.py startapp polls"
    context={'text':text}
    return render(request,'index.html' ,context)