from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable1": "sanya",
        "variable2": "satyam"
    }
    
    return render(request, 'index.html', context)
    

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is service")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your form has been submitted successfully!')

    return render(request, 'contact.html')
    # return HttpResponse("This is contact")