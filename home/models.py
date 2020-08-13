from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.forms import TextInput, ModelForm,Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=150,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    fax = models.CharField(max_length=15,blank=True)
    email = models.CharField(max_length=50,blank=True)
    smtpserver = models.CharField(max_length=20,blank=True)
    smtpsemail = models.CharField(max_length=20,blank=True)
    smtppassword = models.CharField(max_length=10,blank=True)
    smtpport = models.CharField(max_length=5,blank=True)
    icon=models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(max_length=150,blank=True)
    Instagram = models.CharField(max_length=150,blank=True)
    twitter= models.CharField(max_length=150,blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contactus = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS= (
        ('New','New'),
        ('Read','Read'),
        ('Closed', 'Closed'),
    )
    name=models.CharField(blank=True,max_length=20)
    email=models.CharField(blank=True,max_length=50)
    subject=models.CharField(blank=True,max_length=50)
    message=models.CharField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip=models.CharField(blank=True,max_length=20)
    note=models.CharField(blank=True,max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model=ContactFormMessage
        fields=['name','email','subject','message']
        widgets={
            'name':TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input','placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input','placeholder': 'Email Address'}),
            'message': Textarea(attrs={'class': 'input','placeholder': 'Your Message','rows':'5'}),

        }


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True, max_length=20)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username
    def user_name(self):
        return self.user.first_name +' '+ self.user.last_name

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['phone','address','city','country','image']