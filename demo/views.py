from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def insidelayout(request):
    return render(request,'base.html')

def chart(request):
    return render(request,'charts.html')






    
