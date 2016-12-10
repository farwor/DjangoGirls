from django.shortcuts import render
from .models import Post
# Create your views here.

def blogmaian(request):
    list_articles=Post.objects.all()

    return render(request, 'blog/post_list.html', {'list_articles':list_articles})
