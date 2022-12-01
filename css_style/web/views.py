from django.shortcuts import render,redirect
from . models import Student

# Create your views here.
def index(request):
	data=Student.objects.all()
	return render(request,'index.html',{'data':data})

def add(request):
	return render(request,'add.html')

def addstu(request):
	n=request.POST['name']
	e=request.POST['email']
	c=request.POST['city']
	ad=Student(name=n,email=e,city=c)
	ad.save()
	return redirect('index')

def edit(request,id):
	d=Student.objects.get(id=id)
	return render(request,'edit.html',{'d':d})

def update(request,id):
	n=request.POST['name']
	e=request.POST['email']
	c=request.POST['city']
	d=Student.objects.get(id=id)
	d.name=n
	d.email=e
	d.city=c 
	d.save()
	return redirect('index')
	

def delete(request,id):
	d=Student.objects.get(id=id)
	d.delete()
	return redirect('index')
