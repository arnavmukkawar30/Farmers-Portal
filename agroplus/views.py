from django.shortcuts import redirect, render,HttpResponse
from agroplus.models import Sell
from datetime import datetime
import requests
import pandas as pd 
import json

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
    # data = pd.read_csv("../project/static/dataset.csv")
    # pune_data = data[data['district']=='Pune']
    # html_table = dataframe.to_html()
    dataframe = pd.read_csv("./static/dataset.csv")
    search = 'a'
    if request.method == 'POST':
        search = request.POST.get('district')
        print(search)
        if(search != 'a'):
            dataframe = dataframe[dataframe["District"] == search]
            dataframe = dataframe
        # elif(len(search) <= 1):
        #     # dataframe = dataframe[dataframe["District"] == search]
        #     print(dataframe)
        #     # dataframe = pd.read_csv("./static/dataset.csv")
    else:
         dataframe = pd.read_csv("./static/dataset.csv")
         
    json_records = dataframe.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    
    return render(request, 'croprate.html', context)



    # context = {
    #     'html_table' : html_table,
    #     'data' : data,
    #     'cols' : data.columns,
    #     'row_len' : len(data),
    #     'col_len' : len(data.columns)
    # }

    # return render(request,'croprate.html', context=context)
    # return render(request,html_table, context=context)
    # return HttpResponse(html_table)

