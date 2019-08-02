import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

# Create your views here.
# dojo/views.py


# def mysum(request, numbers):
#     numbers=sum(map(lambda s: int(s or 0), numbers.split('/')))
#     return HttpResponse(numbers)

# def hello(request, name, age):
#     produce = '안녕하세요. %s. %s살이시네요' %(name,age)
#     return HttpResponse(produce)
#
from .models import Post
from .forms import PostForm


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>정성모</h1>
    <p>{name}</p>
    <p>여러분의 파이썬 </p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list2.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 나는 장고라고해?',
        'items': ['파이썬', '장고', 'celery']
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = '\pythonPiro\Djangopractice\startproject1/gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')  # 절대경로 바로 아래있는 파일이름
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('dojo:dojo')

    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })



def post_edit(request, id):
    post= get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # print(form.cleaned_data)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('dojo:dojo')

    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })
