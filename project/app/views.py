from django.shortcuts import render
from django .http import HttpResponse
from.models import Student
# Create your views here.
def home(request):
    return render(request,'home.html')

def insert(request):
    Fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']
    print(Fname,lname,email,contact)
    Student.objects.create(
        Firstname=Fname,
        Lastname=lname,
        Email=email,
        Contact=contact
    )
   
    return render(request,'home.html')

def show(request):
    data=Student.objects.all()
    # for i in data:
    #     print(i.id,i.Firstname,i.Lastname)
    return render(request,'show.html',{'user':data})

def editpage(request,pk):
    data=Student.objects.get(id=pk)
    return render(request,'edit.html',{'user':data})

def edit(request,pk):
    user=Student.objects.get(id=pk)
    user.Firstname=request.POST['fname']
    user.Lastname=request.POST['lname']
    user.Email=request.POST['email']
    user.Contact=request.POST['contact']
    user.save()
    data=Student.objects.all()
    return render(request,'show.html',{'user':data})


def deletepage(request,pk):
    user=Student.objects.get(id=pk)
    user.delete()
    data=Student.objects.all()
    return render(request,'show.html',{'user':data})
    
