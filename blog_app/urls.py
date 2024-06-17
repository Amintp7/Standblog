from django.urls import path
from . import views


app_name ="blog_app"
urlpatterns =[
    path('details/<slug:slug>',views.article_details,name="article_details"),
    path('list/',views.articles_list,name='articles_list'),
    path('category/<int:pk>',views.category_detail,name="category_detail"),
    path('search/',views.search,name="search_articles"),
    path('contactus',views.contactus,name="contact_us"),
    path('like/<slug:slug>/<int:pk>',views.like,name="like"),
]