from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import product
from . forms import productform

# Create your views here.
def index(request):
    prod=product.objects.all()
    context={
        'product_hunt':prod
    }
    return render(request,'index.html',context)

def detail(request,product_id):
    prod=product.objects.get(id=product_id)
    return render(request,'detail.html',{'prod':prod})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        rate=request.POST.get('rate')
        img=request.FILES['img']
        prod=product(name=name,desc=desc,rate=rate,img=img)
        prod.save()
    return render(request,'add.html')

def update(request,id):
    prod=product.objects.get(id=id)
    form=productform(request.POST or None,request.FILES, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'product':prod})

def delete(request,id):
    if request.method=='POST':
        prod=product.objects.get(id=id)
        prod.delete()
        return redirect('/')
    return render(request,'delete.html')