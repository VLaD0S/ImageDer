from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def upload_home(request):
    return HttpResponse('<p>Hello World</p>')


def upload_create(request):
    return HttpResponse('<p>Create World</p>')


def upload_detail(request):
    queryset = Post.objects.all()

    context_data = {
        "object_list": queryset,
        "title": "Detail"
    }
    return render(request, "index.html", context_data)


def upload_list(request):
    context_data = {
        "title": "List"
    }
    return render(request, "index.html", context_data)



def upload_delete(request):
    return HttpResponse('<p>Delete World</p>')
