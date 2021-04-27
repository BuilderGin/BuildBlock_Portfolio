from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, CompanyInformation
from .forms import Contact_BerichtForm

def contact(request):

    form = Contact_BerichtForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = Contact_BerichtForm()
            messages.success(request, 'Bedankt voor uw bericht, Ik nemen binnenkort contact met u op.')

    try:
        company = CompanyInformation.objects.get(id=1)
    except:
        company = []

    context = {
        'form':form,
        'company': company,
    }
    return render(request, 'contact/contact.html', context)


# def contact(request):
#     if request.method == 'POST':
#         form = Contact_BerichtForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             form = Contact_BerichtForm()
#             messages.success(request, 'Bedankt voor uw bericht, Ik nemen z.s.m. contact met u op.')
        
#     return render(request, 'contact/contact.html', {'form':form})
