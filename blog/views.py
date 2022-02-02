from multiprocessing import context
from re import template
from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Navbar, main_menu
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.http import Http404
from django.contrib import messages

def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Post.objects.filter(status = 'published')
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        post = post.filter(category=category)
        paginator = Paginator(post, 1)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    template = 'blog/category/list_of_post_by_category.html'
    context = {'categories': categories, 'post': posts, 'category': category}
    return render(request, template, context)

def list_of_post(request):
    post = Post.objects.filter(status='published')
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'blog/post/list_of_post.html'
    context = {'posts': posts, 'page': page}
    return render(request, template, context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    if post.status == 'published':
        template = 'blog/post/post_detail.html'
        return render(request, template, context)
    else:
        template = 'blog/post/post_preview.html'
        return render(request, template, context)

def navbar(request):
    menu_items = Navbar.objects.all()
    template = 'blog/base.html'
    context = {'menuitems': menu_items}
    return render(request, template, context)

def maninmenu(request):
    menu = main_menu.objects.all()
    return render(request, 'blog/base.html', {'menu': menu})



'''def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'blog/post/add_comment.html'
    context = {'form': form}
    return render(request, template, context)'''

########
#backend
########

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    template = 'blog/backend/new_post.html'
    context = {'form':form}
    return render(request, template, context)

def list_of_post_backend(request):
    post = Post.objects.all()
    paginator = Paginator(post, 20)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'blog/backend/list_of_post_backend.html'
    context = {'posts': posts, 'page': page}
    return render(request, template, context)

def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('list_of_post_backend')
    else:
        form = PostForm(instance=post)
    template = 'blog/backend/new_post.html'
    context = {'form': form}
    return render(request, template, context)

def delete_post(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Successfully Delete")
    return redirect('list_of_post_backend')