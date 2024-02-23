from django.contrib import messages
from django.shortcuts import render


def alertMessage(request):
    return render(request, "AlertApp/Alert.html")

def success(request):
    messages.success(request, "This is a success message")
    return render(request, "AlertApp/Alert.html")

def error(request):
    messages.error(request, "This is a error message")
    return render(request, "AlertApp/Alert.html")

def info(request):
    messages.info(request, "This is a information message")
    return render(request, "AlertApp/Alert.html")

def warning(request):
    messages.warning(request, "This is a warning message")
    return render(request, "AlertApp/Alert.html")
