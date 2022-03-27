from django.shortcuts import render

from .logic import calculate

# Create your views here.
def home(request):

    return render(request,'home.html')

def add(request):

    x = request.GET['answer']

    res = calculate(x)

    return render(request,'home.html',{'result':res})