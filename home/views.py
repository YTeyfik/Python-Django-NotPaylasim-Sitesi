import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Note.models import Note, Category, Images, Comment
from content.models import Content, Menu, CImages
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage


# Create your views here.
def index(request):
    setting= Setting.objects.get(pk=1)
    sliderdata=Note.objects.all()[:3]
    category=Category.objects.all()
    menu=Menu.objects.all()
    daynotes=Note.objects.all()[:4]
    lastnotes = Note.objects.all().order_by('-id')[:4]
    randomnotes = Note.objects.all().order_by('?')[:4]
    news=Content.objects.filter(type='haber').order_by('-id')[:4]
    announcements=Content.objects.filter(type='duyuru').order_by('-id')[:4]
    context={'setting':setting,
             'category':category,
             'news':news,
             'announcements':announcements,
             'menu':menu,
             'page':'home',
             'sliderdata':sliderdata,
             'daynotes':daynotes,
             'lastnotes':lastnotes,
             'randomnotes':randomnotes,
             }
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

def note_detail(request,id,slug):
    category = Category.objects.all()
    note = Note.objects.get(pk=id)
    images=Images.objects.filter(note_id=id)
    comments=Comment.objects.filter(note_id=id,status='True')
    context = {'category': category,
               'images':images,
                'note': note,
               'comments':comments,
               }
    return render(request,'note_detail.html',context)


def note_search(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            query=form.cleaned_data['query'] #formdan bilgiyi al
            notes=Note.objects.filter(title__icontains=query) #select from like query
            context={
                'notes':notes,
                'category':category,
            }
            return render(request,'notes_search.html',context)
    return  HttpResponseRedirect('/')


def note_search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    note = Note.objects.filter(title__icontains=q)
    results = []
    for rs in note:
      note_json = {}
      note_json = rs.title
      results.append(note_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Kullanıcı adı yada parola yanlış")
            return HttpResponseRedirect('/login')


    category = Category.objects.all()
    context = {
        'category': category,
    }

    return render(request,'login.html',context)

def signup_view(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect('/')

    form=SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form':form,
    }

    return render(request,'signup.html',context)

def menu(request,id):
    try:
        content=Content.objects.get(menu_id=id)
        link='/content/'+str(content.id)+'menu'
        return HttpResponseRedirect(link)
    except:
        messages.warning(request,"Hata!")
        link ='/'
        return HttpResponseRedirect(link)

def contentdetail(request,id,slug):
    category=Category.objects.all()
    menu=Menu.objects.all()
    content=Content.objects.get(pk=id)
    images=CImages.objects.filter(content_id=id)


    context={
        'content':content,
        'category':category,
        'menu':menu,
        'images':images,
    }
    return render(request,'content_detail.html',context)
