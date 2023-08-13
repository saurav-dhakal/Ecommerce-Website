from django.shortcuts import render
from .models import Folder,Order,Message
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    
 
    return render(request,'home.html')

def test(request):
    
 
    return render(request,'test.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    if request.method =="POST":
       
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        message=request.POST.get('message','')
        Message(name=name,email=email,message=message).save()
        
    return render(request,'contact.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def deliverypolicy(request):
    return render(request,'deliverypolicy.html')

def folder(request):
    
    f=Folder.objects.all()
 
    forward = {'product':f}
    return render(request,"options.html",forward)
    

def orderform(request,id):
    product = get_object_or_404(Folder, product_id=id)
    price=product.price
    forward = {'product':product, 'id':id,'price':price}
    return render(request,"orderform.html",forward)
    
def orderfolder(request,id):
    product=get_object_or_404(Folder, product_id=id)
    product_name=product.product_name
    image=product.main_image
    product.stock=product.stock -1
    product.save()
    
    if request.method =="POST":
       
        size=request.POST.get('size','')

        quantity=request.POST.get('quantity','')
        addinfo=request.POST.get('addinfo','')
        name=request.POST.get('name','')
        contact=request.POST.get('contact','')
        location=request.POST.get('location','')
        

        Details=Order( size=size, quantity=quantity, addinfo=addinfo, contact=contact, location=location, name=name,product_name=product_name, image=image)
        Details.save()
        
    
    price=product.price 
    
    tprice=(int(price) * int(quantity)) + 99 
    forward = {'product':product, 'id':id,'quantity':quantity,'tprice':tprice,}

    return render(request,"ordersummary.html",forward)