from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def reference(request):
    return render(request, 'frontend/reference.html')

def toeic(request):
    return render(request, 'frontend/toeic.html')

def cert(request):
    return render(request, 'frontend/cert.html')



