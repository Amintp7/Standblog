from django.shortcuts import render
from blog_app.models import Article



def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()
    return render(request,'home_app/home.html',context={'articles':articles,'recent_articles':recent_articles})



def sidebar(request):
    data = {'name':'amin'}
    return render(request,'includes/sidebar.html',context=data)