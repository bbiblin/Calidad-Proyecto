from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def index(request):
    return render(request, "pages/index.html")