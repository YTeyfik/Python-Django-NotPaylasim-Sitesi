from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting
# Create your views here.
def index(request):
    setting= Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request,'index.html' ,context)

def about(request):
    setting= Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request,'about.html' ,context)

def reference(request):
    setting= Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'reference.html', context)
def contact(request):
    setting= Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'contact.html', context)