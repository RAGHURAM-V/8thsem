from django.shortcuts import render



def chart_view(request):
    print(request.headers)
    return render(request, "charts.html",{})





    