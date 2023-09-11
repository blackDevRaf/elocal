from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Order,ProductImages


# Create your views here.
def home(request):
    

    products=Product.objects.all()
    return render(request,"core/index.html",{"products":products})


def product(request,pk):

    
    if request.method=="POST":
        pro=Product.objects.get(pk=pk)
        phone=request.POST["phone"]
        adrees=request.POST["adrees"]
        city=request.POST["city"]
        talab=Order(product=pro,phone=phone,adrees=adrees,city=city,total=pro.price)
        talab.save()
        return HttpResponse("thank u for your order")

    else:
        pass

    product=Product.objects.get(pk=pk)
    pics=ProductImages.objects.filter(product=product)
    context={"product":product,
              "pics":pics
            }
    return render(request,"core/product_detaile.html",context)



    


