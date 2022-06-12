from django.shortcuts import redirect, render,HttpResponse
from agroplus.models import Sell
from datetime import datetime
import requests


# Create your views here.
def home(request):
    return render(request, 'home.html')

def farmercorner(request):
    return render(request, 'farmercorner.html')

def Buy(request):
    data = Sell.objects.all()
    return render(request, 'Buy.html',{'data': data})

def SellFun(request):
    if request.method == "POST":
        SellerName = request.POST.get('SellerName')
        CropName = request.POST.get('CropName')
        # Image = request.POST.get('Image')
        Image = request.FILES.get('Image')
        Price = request.POST.get('Price')
        Description = request.POST.get('Description')
        imgpath = request.POST.get('imgpath')
        # imgpath = 'media/'+imgpath
        # if(not Image):
        #     Image= "static/Sell_images/AGROPLUS.png"
        sell = Sell(SellerName=SellerName,CropName=CropName,Image=Image,Price=Price,Description=Description,imgpath=imgpath,date=datetime.now())
        sell.save()
        return redirect('Buy')
    return render(request, 'Sell.html')

def Croprate(request):
    if request.method == 'POST':
        response=requests.get("https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001d9ba49cdb430411759aaafa37e2fe03b&format=json&limit=543").json()
        response = response["records"]
        return render(request, 'croprate.html',{'response': response})
    return render(request, 'croprate.html')


