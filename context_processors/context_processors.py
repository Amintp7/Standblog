from blog_app.models import Article,Category

def recent_arts(request):
    recent_arts = Article.objects.order_by('-created')
    categories =Category.objects.all()
    return {'recent_arts':recent_arts,'categories':categories}