from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def insidelayout(request):
    return render(request,'layout.html')

def chart(request):
    return render(request,'charts.html')






    