from django.shortcuts import render



def index(request):
    return render(request,'index.html')
def buysell(request):
    return render(request,'buysell.html')

def insidelayout(request):
    return render(request,'layout.html')

def chart(request):
    return render(request,'charts.html')






    