from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Blog

# Create your views here.

# def blog(request):
#     blog = Blog.objects.all()

#     context = {'blog':blog}
#     return render(request, 'index.html', context)

class BlogsList(ListView):
    model = Blog
    paginate_by = 2
    template_name = 'index.html'


class BlogDetails(DetailView):
    model = Blog
    template_name = 'blog-view.html'
