from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .models import Article, Tag, Category
from .forms import CommentForm


def index(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    articles = Article.objects.order_by('-id')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(3)
    ctx = {
        'object_list': page_obj,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'wordify/index.html', ctx)


def article_list(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    articles = Article.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(3)
    ctx = {
        'object_list': page_obj,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'wordify/blog.html', ctx)


def category(request):
    articles = Article.objects.all().order_by('id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    qwer = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(3)
    ctx = {
        'object_list': page_obj,
        'tags': tags,
        'categories': categories,
        'qwer': qwer

    }
    return render(request, 'wordify/category.html', ctx)


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    last_3_articles = Article.objects.order_by('-id')[:3]
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render(request, 'html')
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    ctx = {
        'object': article,
        'categories': categories,
        'last_3_articles': last_3_articles,
        'tags': tags,
        'form': form,
    }
    return render(request, 'wordify/blog-single.html', ctx)




