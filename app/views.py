from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fruit(request):
    return render(request,'fruit.html')

def favourite(request):
    return render(request,'favourite.html')