from django.shortcuts import render
from datetime import datetime

from django.template.context_processors import request

from .models import SampleTable, StudentsInfo


def IPLTable(request):
    date = datetime.now()
    details = {'year' : '2024','name' : 'TATA', 'country' : 'INDIA', 'location' : 'chennai', 'date':date}
    return  render(request,r'SecondWebApp/IPLTable.html',context= details)

def products(request):
    return  render(request, r'SecondWebApp/ProductDetails.html')

def price(request):
    keyboard = int(request.GET["keyboard"])
    laptop = int(request.GET["laptop"])
    mobile = int(request.GET["mobile"])
    mouse = int(request.GET["mouse"])
    tablet = int(request.GET["tablet"])

    totalPrice = keyboard + laptop + mobile + mouse + tablet
    finalprice = {'price' : totalPrice}
    return  render(request, r'SecondWebApp/TotalPrice.html', context= finalprice)


def getsample(request):
    sampletable = SampleTable.objects.all()
    sample = {"sampleTable" : sampletable}
    return render(request, r'SecondWebApp/Sample.html', context= sample)


def getstudentinfo(request):
    stdinfo = StudentsInfo.objects.all()
    students = {"info" : stdinfo}
    return render(request, r'SecondWebApp/Students.html', context= students)