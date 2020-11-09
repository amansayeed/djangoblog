from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

posts=\
    [
        { 'author': 'aman Sayeed',
            'title': 'this is the first post ',
          'content' :' lfdkfnlnbfl slkndlfnlfdnbl lksnvflnfdls',

         'date': '20/10/2020',

         },

{ 'author': 'asad  Sayeed',
            'title': 'this is the secound post ',
          'content' :' lfdkfnlnbfl slkndlfnlfdnbl sdvksjdhsfssllsh lksnvflnfdls',

         'date': '26/10/2020',

         }
    ]

context= {
    'posts': posts
}


def home(request):
    # return  HttpResponse('<h1>this is blog home</h1> ')
    return  render(request, 'blog/home.html', context)

def about(request):
    # return  HttpResponse('<h1>this is blog about page </h1> ')
        return render(request, 'blog/about.html')

