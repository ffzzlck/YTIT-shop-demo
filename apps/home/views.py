from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Title, Products, Products1, Goods, Category, Tags
from apps.comments.forms import CommentForm


def product_single(request):
    return render(request, 'product-detail.html')


def index(request):
    titles = Title.objects.all().order_by('-id')
    categories = Category.objects.all()
    object_list = Products.objects.all().order_by('-id')
    object_list1 = Products1.objects.all().order_by('-id')
    goods = Goods.objects.all().order_by('-id')
    posts = Products.objects.all()
    for category in categories:
        category.n = len(Products.objects.filter(category=category))
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    context = {
        'titles': titles,
        'categories': categories,
        'object_list': object_list,
        'object_list1': object_list1,
        'goods': goods,
        'p': p,
        'posts': posts_,
        'posts_category': posts[:3:-1],
    }
    return render(request, 'index.html', context)


def views_up(request, pk):
    product = Products.objects.get(id=pk)
    product.save()
    return redirect('home:detail', product.pk)


def product_detail(request, pk):
    goods = Products.objects.get(id=pk)
    categories = Category.objects.all()
    related_products = Products.objects.all().order_by('-id')[:3]
    tags = Tags.objects.all()
    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article_id = pk
        obj.save()
        return redirect(f'/blog-detail/{pk}#article-comments')
    context = {
        'goods': goods,
        'categories': categories,
        'related_products': related_products,
        'tags': tags,
        'form': form,
    }
    return render(request, 'product-detail.html', context)


def product_view(request):
    products = Products.objects.all().order_by('-id')
    tag = request.GET.get('tag')
    category = request.GET.get('category')
    q = request.GET.get('q')
    if tag:
        products = products.filter(tags__title__exact=tag)
    if category:
        products = products.filter(category__title__exact=category)
    if q:
        products = products.filter(title__exact=q)

    context = {
        'products': products,

    }
    return render(request, 'product.html', context)
