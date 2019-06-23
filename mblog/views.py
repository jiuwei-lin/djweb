from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.


def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    now = datetime.now()
    return render(request, 'mblog.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)

        if post != None:
            return render(request, 'mblog_post.html', locals())
    except:
        return redirect('/')


""" 
Samle: HttpResponse

    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
        post_lists.append(
            "<small>{}</small><br/><br/>".format(str(post.body)))

    return HttpResponse(post_lists)
"""
