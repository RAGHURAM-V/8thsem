from django.shortcuts import render

from django.views.generic import View 

from rest_framework.views import APIView 
from rest_framework.response import Response 

class HomeView(View): 
	def get(self, request, *args, **kwargs): 
		return render(request, 'chart.html') 




class ChartData(APIView): 
	authentication_classes = [] 
	permission_classes = [] 

	def get(self, request, format = None): 
		labels = [ 
			'January', 
			'February', 
			'March', 
			'April', 
			'May', 
			'June', 
			'July',
			'August',
			'September',
			'October'
			] 
		chartLabel = "my data"
		chartdata = [0, 10, 5, 2, 20, 30, 45,10,50,27,67,90,65,45,32,53,13,52,15,78] 
		data ={ 
					"labels":labels, 
					"chartLabel":chartLabel, 
					"chartdata":chartdata, 
			} 
		return Response(data) 


def index(request):
    return render(request,'index.html')
def buysell(request):
    return render(request,'buysell.html')

def insidelayout(request):
    return render(request,'layout.html')

def chart(request):
    return render(request,'charts.html')






    
