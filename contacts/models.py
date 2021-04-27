from django.db import models
from datetime import datetime

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    message = models.TextField(blank=False)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name


class CompanyInformation(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    adres = models.CharField(max_length=50)

    completed_projects = models.IntegerField()
    perspectief_clients = models.IntegerField()
    happy_clients = models.IntegerField()
    about_me = models.TextField(max_length=255)


class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(max_length=146)
    person_name = models.CharField(max_length=50)
    person_function = models.CharField(max_length=50)
    person_Profile = models.ImageField(default="/hello.png/")
    upload_date = models.DateTimeField(default=datetime.now, blank=True)


class Portfolio(models.Model):

    CATEGORY_CHOICE = [
        ('eCommerce / Django', 'eCommerce Django'),
        ('Portfolio', 'Portfolio'),
        ('Website', 'Website'),
        ('LogoDesign', 'LogoDesign'),
        ('WebDesign', 'WebDesign'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    image = models.ImageField()
    website_link = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICE)
    upload_date = models.DateTimeField(default=datetime.now, blank=True)


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    icon = models.ImageField()
    description = models.TextField(max_length=146)
    upload_date = models.DateTimeField(default=datetime.now, blank=True)

class ServicesLogos(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    company_logo = models.ImageField()
    website_link = models.CharField(max_length=255)
    upload_date = models.DateTimeField(default=datetime.now, blank=True)