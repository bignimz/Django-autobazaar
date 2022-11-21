from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def inventory(request):
    return render(request,'inventory.html')

def car_detail(request):
    return render(request,'car_detail.html')

def dealers(request):
    return render(request, 'dealers.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')

def faq(request):
    return render(request, 'faq.html')