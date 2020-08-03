

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Note.models import Note,Category
from home.models import Setting, ContactFormu, ContactFormMessage


# Create your views here.
def index(request):
    setting= Setting.objects.get(pk=1)
    sliderdata=Note.objects.all()[:3]
    category=Category.objects.all()

    context={'setting':setting,
             'category':category,
             'page':'home',
             'sliderdata':sliderdata}
    return render(request,'index.html' ,context)

def about(request):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()

    context={'setting':setting,'category': category}
    return render(request,'about.html' ,context)

def reference(request):
    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    context={'setting':setting,'category': category}
    return render(request, 'reference.html', context)

def contact(request):
    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarı ile gönderilmiştir.Teşekkür Ederiz")
            return  HttpResponseRedirect('/contact')

    setting= Setting.objects.get(pk=1)
    category = Category.objects.all()
    form=ContactFormu()
    context={'setting':setting,'form':form,'category': category}
    return render(request, 'contact.html', context)

def category_notes(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    notes=Note.objects.filter(category_id=id)
    context={'notes':notes,
             'category':category,
             'categorydata':categorydata
             }
    return render(request,'notes.html',context)