from django.shortcuts import render,get_object_or_404,redirect
from blog_app.models import Article,Category,Comment, Like, Message
from django.core.paginator import Paginator
from .forms import ContactUsForm,MessageForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView



def article_details(request,slug):
    articles = get_object_or_404(Article,slug=slug)
    # if request.method == 'POST':
    #     parent_id = request.POST.get('parent_id')
    #     body = request.POST.get('body')
    #     Comment.objects.create(body=body,article=articles,user=request.user,parent_id=parent_id)
    
    return render(request,'blog_app/article_details.html',context={'articles':articles})


        


def articles_list(request):
    article_list = Article.objects.all()
    page_number = request.GET.get('page') #for pagination(episode 96)
    paginator = Paginator(article_list,1)
    objects_list = paginator.get_page(page_number)
    return render(request,'blog_app/articles_list.html',context={'article_list':objects_list})


def category_detail(request,pk=None):
    category = get_object_or_404(Category,id=pk) #instead of "Category.objects.all() "(episode93)
    articles = category.articles.all() #default is"articles =category.article_set.all()" but for being easy we change the 'article_set' to articles with related_name in models
    return render(request,'blog_app/articles_list.html',{'article_list':articles})



def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q )
    page_number = request.GET.get('page') #for pagination(episode 96)
    paginator = Paginator(articles,1)
    objects_list = paginator.get_page(page_number)
    return render(request,'blog_app/articles_list.html',context={'article_list':objects_list})




def contactus(request):
    if request.method =='POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = MessageForm()
    return render(request,'blog_app/contact_us.html',context={'form':form})


def like(request,slug,pk):
    try:
        like = Like.objects.get(article__slug=slug,user_id=request.user.id)
        like.delete()
    except:
        like = Like.objects.create(article_id=pk,user_id=request.user.id)
    return redirect('blog_app:article_details',slug)


# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = "blog_app/article_details.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.user.likes.filter(article__slug=self.object.slug,user_id=self.request.user.id).exists():
#             context['is_liked'] = True
#         else:
#             context['is_liked'] = False


#         return context