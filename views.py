from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage(/home)")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("This is my about page(/about)")
    return render(request,'about.html')
def projects(request):
    #return HttpResponse("This is my project page(/project)")
    return render(request,'projects.html')

def contact(request):
    if request.method=='POST':        
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        #print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the db")
    #return HttpResponse("This is my contact page(/contact)")
    return render(request , 'contact.html')