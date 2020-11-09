from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return  HttpResponse('<h1>this is blog home</h1> ')
    return  render(request, 'blog/home.html')

def about(request):
    # return  HttpResponse('<h1>this is blog about page </h1> ')
        return render(request, 'blog/about.html')

