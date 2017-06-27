from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostCreateForm
from .models import Post    


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # assign the current user to new post
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Post created successfully')
            # redirect to the newly created post
            return redirect(new_item.get_absolute_url())
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'posts/post/create.html', {'section': 'posts',
                                                           'form': form})


def post_detail(request, id):
   post = get_object_or_404(Post, id=id) 
   return render(request, 'posts/post/detail.html', {'section': 'posts',
                                                       'post': post})


@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ok'})

@login_required
def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse('')
        posts = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'posts/post/list_ajax.html',
                {'section': 'posts', 'posts': posts})
    return render(request, 'posts/post/list.html', 
            {'section': 'posts', 'posts': posts})


