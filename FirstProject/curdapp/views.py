from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import EmployeeRegisterForm
from .models import EmployeeRegister


def getEmployeeDetails(request):
    empDetails = EmployeeRegister.objects.all()
    data = serializers.serialize("json", empDetails)
    return HttpResponse(data, content_type="application/json")
    # return render(request, "CurdApp/employeedetails.html", context={"empDetails" : empDetails})

def createnewemployee(request):
    form = EmployeeRegisterForm()
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>New Data Added successfuly. <a href = '/curd/emp'>Click here</a></h1>")
    return render(request, "CurdApp/addemployeedetails.html", context={"form" : form})

def delete_Employee(request, id):
    empdetails = EmployeeRegister.objects.get(id = id)
    empdetails.delete()
    return redirect("/curd/emp")
    # return HttpResponse('Employee data Deleted successfully<h1><a href = "/curd/emp">Click here to view table</a></h1>')

# def update_Employee(request, id):
#     empdetails = EmployeeRegister.objects.get(id=id)
#     if request.method=="POST":
#         form=EmployeeRegisterForm(request.POST, instance=empdetails)
#         if form.is_valid():
#             form.save()
#             return HttpResponse(
#                 "<h1>Employee data successfully updated<a href = '/curd/emp'>Click here to view table</a></h1>")
#     return render(request, "CurdApp/updateemployee.html", context={"empdetails":empdetails})

def updateEmployee(request, id):
    employee = EmployeeRegister.objects.get(id = id)

    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Updated data</h1>")
    return render(request, "CurdApp/updateemployee.html", context={"employee" : employee})