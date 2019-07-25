from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


# Create your views here.

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {'post_list': qs, 'q': q})


def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    #post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def create(request):
    if request.POST:
        new_post = Post()
        new_post.user = request.GET['user']
        new_post.title = request.GET['title']
        new_post.content = request.GET['content']
        new_post.save()
    return redirect()