from django.shortcuts import render
from .models import Product, Inquiry

def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Inquiry.objects.create(name=name, email=email, message=message)
    return render(request, 'main/contact.html')

def calculator(request):
    return render(request, 'main/calculator.html')

def login(request):
    return render(request, 'main/login.html')
