from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "pages/home.html")

def index(request):
    return render(request, "pages/index.html")

def gestionResidentes(request):
    return render(request, "pages/gestionResidentes.html")

def gestionSalidas(request):
    return render(request, "pages/gestionSalidas.html")

def gestionMedicamentos(request):
    return render(request, "pages/gestionMedicamentos.html")

def detalleMedicamentos(request):
    return render(request, "pages/detalleMedicamentos.html")