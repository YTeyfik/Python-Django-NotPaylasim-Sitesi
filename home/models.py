from django.db import models

# Create your models here.

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
    aboutus = models.TextField(blank=True)
    contactus = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title