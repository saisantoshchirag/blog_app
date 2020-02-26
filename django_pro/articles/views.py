from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.filter(type='Public').order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})
def article_detail(request,slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()

    return render(request, "articles/article_create.html",{'form':form})

def my_articles(request):
    articles = Article.objects.filter(author=request.user)
    print(articles)
    return render(request, "articles/my_article.html",{'article':articles})

def search(request):

    if request.method == 'GET':
        query = request.GET.get('search')
        if query is not None:
            total = Article.objects.filter(title__icontains=query,type='Public') | Article.objects.filter(author__username__icontains=query,type='Public')
            context = {'results':total}
            return render(request,'articles/search.html',context)
        else:
            return render(request, 'articles/search.html')
    else:
        return render(request,'articles/search.html')