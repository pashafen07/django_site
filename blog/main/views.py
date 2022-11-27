from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blog.html', {'blogs': blogs})


def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')

    form = BlogForm
    context = {
        'form': form
    }
    return render(request, 'main/new-blog.html', context)
