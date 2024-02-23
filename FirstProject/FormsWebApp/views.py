from django.http import HttpResponse
from django.shortcuts import render

from . import forms
from .models import RegisterModels


def getRegister(request):
    form = forms.RegisterForms()
    return render(request, r'Forms/Register.html', context= {"form": form})

def getRegisterModels(request):
    if request.method == 'POST':
        if(request.POST.get('Firstname')
                and request.POST.get('Lastname') and request.POST.get('Email')
                and request.POST.get('Password') and request.POST.get('Confirm_password')):
            reg = RegisterModels()
            reg.Firstname = request.POST.get('Firstname')
            reg.Lastname = request.POST.get('Lastname')
            reg.Email = request.POST.get('Email')
            reg.Password = request.POST.get('Password')
            reg.Confirm_password = request.POST.get('Confirm_password')
            reg.save()
            return HttpResponse('Sucess')
        else:
            return HttpResponse('Some fields are missing')
    form = forms.RegisterForms()
    return render(request, r'Forms/Register.html', context= {"form": form})

def getUser(request):
    form = forms.UserForms()
    return render(request, r'Forms/User.html', context= {"form": form})