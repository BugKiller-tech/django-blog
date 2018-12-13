from django.shortcuts import render
from django.http import HttpResponse


posts = [
  {
    'author': 'Corey',
    'title': 'blog post1',
    'content': 'first blog post',
    'date_created': 'aug 27, 2018'
  },
  {
    'author': 'Corey 222',
    'title': 'blog post1',
    'content': 'first blog post',
    'date_created': 'aug 27, 2018'
  }
]

# Create your views here.

def home(request):
  # return HttpResponse('<h1>welcome to my blog</h1>')
  context = {
    'title': 'latest blogs',
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')

def error_404(request):
  return HttpResponse('<h1>Page not found!</h1>', { 'title': 'about page' })