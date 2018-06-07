from django.shortcuts import render

# Create your views here
from django.utils import timezone
from .models import Post


def main(req):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(req, 'blog/main.html', {'posts':posts})

def board_1(req):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(req, 'blog/board_1.html', {'posts':posts})
