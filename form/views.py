from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import PostModel

def index(request):
    posts = PostModel.objects.all()
    context = {
        'page_title':'List Post',
        'posts':posts,
    }
    return render(request, 'form/index.html', context)

def create(request):
    post_form = PostForm()

    if request.method == 'POST':
        PostModel.objects.create(
            judul = request.POST.get('judul'),
            body = request.POST.get('body'),
            category =request.POST.get('category'),
        )

        return HttpResponseRedirect("/form/")

    context = {
        'page_title': 'List Post',
        'post_form':post_form
    }
    return render(request, 'form/create.html', context)